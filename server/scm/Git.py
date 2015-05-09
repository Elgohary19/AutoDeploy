__author__ = 'mohamed'
from BaseSCM import BaseSCM


class GIT(BaseSCM):

    def __init__(self,workdir,repo=""):
        self.workdir=workdir
        self.repo=repo
    def setKey(self,key):
        from os.path import expanduser
        home = expanduser("~")
        keyfile=home+"/.ssh/id_rsa"
        Common.run("chmod 700 %s"%keyfile)
        f=open(keyfile,"w")
        f.write(key)
        f.close()
        Common.run("chmod 400 %s"%keyfile)
    def get_clone_cmd(self):
        return "git clone %s %s"%(self.repo,self.workdir)
    def get_pull_cmd(self):
        return "cd %s; git pull"%self.workdir
    def get_list_tags_cmd(self):
        return "cd %s; git tag -l"%self.workdir
    def get_switch_to_tag_cmd(self,tag):
        return "cd %s; git checkout tags/%s"%(self.workdir,tag)