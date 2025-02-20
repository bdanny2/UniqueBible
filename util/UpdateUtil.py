import os, platform, subprocess, requests, config
import sys
from ast import literal_eval
from util.DateUtil import DateUtil


class UpdateUtil:

    repository = "https://raw.githubusercontent.com/eliranwong/UniqueBible/main/"

    @staticmethod
    def checkIfShouldCheckForAppUpdate():
        if config.lastAppUpdateCheckDate == '':
            config.lastAppUpdateCheckDate = str(DateUtil.localDateNow())
            return False
        else:
            compareDate = DateUtil.addDays(UpdateUtil.lastAppUpdateCheckDateObject(),
                                           int(config.daysElapseForNextAppUpdateCheck))
            if compareDate <= DateUtil.localDateNow():
                return True
            else:
                return False

    @staticmethod
    def lastAppUpdateCheckDateObject():
        return DateUtil.dateStringToObject(config.lastAppUpdateCheckDate)

    @staticmethod
    def getLatestVersion():
        try:
            checkFile = "{0}UniqueBibleAppVersion.txt".format(UpdateUtil.repository)
            request = requests.get(checkFile, timeout=5)
            if request.status_code == 200:
                config.internet = True
                return request.text.strip()
            else:
                config.internet = False
        except Exception as e:
            config.internet = False
        return ""

    @staticmethod
    def getCurrentVersion():
        with open("UniqueBibleAppVersion.txt", "r", encoding="utf-8") as fileObject:
            text = fileObject.read()
            return text.strip()

    @staticmethod
    def currentIsLatest(current, latest):
        if current == '' or latest == '':
            return False
        res = float(current) >= float(latest)
        return res

    @staticmethod
    def updateUniqueBibleApp(parent=None, debug=False):
        if config.updateWithGitPull and os.path.isdir(".git"):
            subprocess.Popen("git pull", shell=True)
        else:
            requestObject = requests.get("{0}patches.txt".format(UpdateUtil.repository))
            for line in requestObject.text.split("\n"):
                if line:
                    try:
                        version, contentType, filePath = literal_eval(line)
                        if version > config.version:
                            localPath = os.path.join(*filePath.split("/"))
                            if debug:
                                print("{0}:{1}".format(version, localPath))
                            else:
                                if contentType == "folder":
                                    if not os.path.isdir(localPath):
                                        os.makedirs(localPath)
                                elif contentType == "file":
                                    requestObject2 = requests.get("{0}{1}".format(UpdateUtil.repository, filePath))
                                    with open(localPath, "wb") as fileObject:
                                        fileObject.write(requestObject2.content)
                                elif contentType == "delete":
                                    try:
                                        if os.path.exists(localPath):
                                            os.remove(localPath)
                                    except:
                                        print("Could not delete {0}".format(localPath))
                    except Exception as e:
                        # message on failed item
                        if parent is not None:
                            parent.displayMessage("{0}\n{1}".format(config.thisTranslation["message_fail"], line))
                        else:
                            return "Could not update"
        # set executable files on macOS or Linux
        if not platform.system() == "Windows":
            for filename in ("uba.py", "main.py", "BibleVerseParser.py", "RegexSearch.py"):
                if os.path.isfile(filename):
                    os.chmod(filename, 0o755)
                # finish message
        config.lastAppUpdateCheckDate = str(DateUtil.localDateNow())
        if parent is not None:
            parent.displayMessage(
                "{0}  {1}".format(config.thisTranslation["message_done"], config.thisTranslation["message_restart"]))
        else:
            return "Success"

    @staticmethod
    def getFilesChanged(sha1, sha2):
        diffCommand = "git diff --name-status {0} {1}".format(sha1, sha2)
        print(diffCommand)
        git = subprocess.Popen(diffCommand, shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = git.communicate()
        files = stdout.decode("utf-8").split("\n")
        return files

    @staticmethod
    def updatePatchFileWithChanges(version, sha1, sha2):
        ver = "{:.2f}".format(float(version))
        lines = UpdateUtil.getFilesChanged(sha1, sha2)
        patch = open("patches.txt", "a")
        for line in lines:
            if not line == "":
                action = "file"
                code, file = line.split("\t")
                if not file in ("patches.txt", "latest_changes.txt", "UniqueBibleAppVersion.txt"):
                    if code.strip() == "D":
                        action = "delete"
                    str = """({0}, "{1}", "{2}")""".format(ver, action, file.strip())
                    print(str)
                    patch.write(str + "\n")
        patch.write("""({0}, "{1}", "{2}")\n""".format(ver, action, "patches.txt"))
        patch.write("""({0}, "{1}", "{2}")\n""".format(ver, action, "latest_changes.txt"))
        patch.write("""({0}, "{1}", "{2}")\n""".format(ver, action, "UniqueBibleAppVersion.txt"))
        patch.close()


if __name__ == "__main__":

    version = "25.63"
    # Run "git log" to find the sha of commits to compare
    sha1 = "7ea151d9e680cd437be03e39e94bf423d0669c0d"
    sha2 = "03916ca2cac9d516f35c33e96688f361ec4b0526"
    if len(sys.argv) == 4:
        version = sys.argv[1].strip()
        sha1 = sys.argv[2].strip()
        sha2 = sys.argv[3].strip()
    elif len(sys.argv) > 1:
        print("python3 -m util.UpdateUtil version sha1 sha2")
        exit(1)
    UpdateUtil.updatePatchFileWithChanges(version, sha1, sha2)

