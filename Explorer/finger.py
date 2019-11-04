import requests
import threading
import re
import requests
import hashlib, sys
import gevent
from gevent.queue import Queue
from gevent import monkey
import time





class WhatCms:
    def __init__(self, target, file_path, thread_num=15):
        self.cms = []
        self.is_finish = False
        self.g_index = 0
        self.threads = []
        self.lock = threading.Lock()
        self.thread_num = thread_num
        self.target = WhatCms.normalize_target(target)
        self.info = {}
        self.file_path = file_path

    @staticmethod
    def request_url(url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
            }
            r = requests.get(url=url, headers=headers)
            r.encoding = 'utf-8'
            if r.status_code == 200:
                return r.text
            else:
                return ''
        except:
            return ''

    @staticmethod
    def normalize_target(target):
        if target.endswith('/'):
            target = target[:-1]
        if target.startswith('http://') or target.startswith('https://'):
            pass
        else:
            target = 'http://' + target
        return target

    def find_powered_by(self):
        '''
        根据powered by获取cms
        :return:
        '''
        html = WhatCms.request_url(self.target)
        match = re.search('Powered by (.*)', html, re.I)
        if match:
            clear_html_cms = re.sub('<.*?>', '', match.group(1))
            cms_name = clear_html_cms.split(' ')[0]
            self.info['cms_name'] = cms_name
            self.info['path'] = '/'
            self.info['match_pattern'] = "powered by " + cms_name
            self.is_finish = True
            return True
        else:
            return False

    def find_cms_with_file(self):
        '''
        根据cms.txt检测cms
        :return:
        '''
        while True:
            if self.is_finish:
                break
            if self.g_index >= len(self.cms):
                self.lock.acquire()
                self.is_finish = True
                self.info['cms_name'] = "nothing"
                self.info['path'] = "nothing"
                self.info['match_pattern'] = "nothing"
                self.lock.release()
                break

            self.lock.acquire()
            try:
                eachline = self.cms[self.g_index]
            except:
                break
            self.g_index += 1
            self.lock.release()

            if len(eachline.strip()) == 0 or eachline.startswith('#'):
                continue
            else:
                path, pattern, cms_name = eachline.split('------')

            url = self.target + path
            response_html = WhatCms.request_url(url)

            if pattern.lower() in response_html.lower():
                self.lock.acquire()
                self.is_finish = True
                self.info['cms_name'] = cms_name[:-1]
                self.info['path'] = path
                self.info['match_pattern'] = pattern
                self.lock.release()
                break

    def start_threads(self):
        for i in range(self.thread_num):
            t = threading.Thread(target=self.find_cms_with_file)
            self.threads.append(t)

        for t in self.threads:
            t.start()

        for t in self.threads:
            t.join()

    def run(self):
        info = self.find_powered_by()
        if not info:
            file = open(self.file_path, 'r')
            self.cms = file.readlines()
            file.close()
            self.start_threads()

    def get_result(self):
        while True:
            if self.is_finish:
                return self.info


monkey.patch_all()


class gwhatweb(object):
    def __init__(self, url, webdata):
        self.tasks = Queue()
        self.url = url.rstrip("/")
        self.cmsdict = {}
        self.cmsname = None
        for i in webdata:
            self.tasks.put(i)

        print("webdata total:%d" % len(webdata))

    def _GetMd5(self, body):
        m2 = hashlib.md5()
        m2.update(body)
        return m2.hexdigest()

    def _clearQueue(self):
        while not self.tasks.empty():
            self.tasks.get()

    def _worker(self):
        data = self.tasks.get()
        test_url = "{0}{1}".format(self.url, data["url"])
        req = None
        try:
            print("[!]spider website {0}".format(test_url))
            req = requests.get(test_url, timeout=10)
            #
            # rtext = req.text
            # if rtext is None:
            #     return
        except:
            rtext = ''

        if not req:
            return False

        result = checkcms(req, data)

        if result:

            if result > 100:
                # logger.info('web is  {0} finger: {1}'.format(data['name'], data['url']))
                return data['name']

            if data['name'] not in self.cmsdict:
                # logger.info('web look like {0}'.format(data['name']))
                self.cmsdict[data['name']] = data['weight']
                # logger.info('cms weight:{}'.format(self.cmsdict[data['name']]))
            else:
                self.cmsdict[data['name']] += data['weight']
                # logger.info('cms weight:{}'.format(self.cmsdict[data['name']]))
                if self.cmsdict[data['name']] > 100:
                    # logger.info('web is  {0} finger: {1}'.format(data['name'], data['url']))

                    return data['name']
        return False

    def _boss(self):
        while not self.tasks.empty():
            flag = self._worker()
            if flag:
                self.cmsname = flag
                self._clearQueue()

    def whatweb(self, maxsize=5):
        allr = [gevent.spawn(self._boss) for i in range(maxsize)]
        gevent.joinall(allr)
        return self.cmsname


def checkcms(req_obj, rule):
    '''
    {"ruletype": "code", "rule": 200, "weight":75}
    :return:
    '''
    # if self.rule['d']
    method = rule['method']
    weight = 0

    if method == 're':
        regu_cont = re.compile(rule['value'], re.I)
        res = regu_cont.match(req_obj.text)
        if res:
            weight = rule['weight']
    elif method == 'md5':
        md5 = _GetMd5(req_obj.text)
        if md5 == rule['value']:
            weight = rule['weight']
    elif method == 'code':
        code = req_obj.status_code
        if code == rule['value']:
            weight = rule['weight']

    return weight
