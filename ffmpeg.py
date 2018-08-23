import os
def formatch(fo,name):
    try:
        command = 'ffmpeg -i \"d:/doco/'+name+'.\"'+fo+' \"d:/doco/'+name+'.mp3\"'
        os.popen(command)
        print('format success~')
    except:
        print('format wrong~')
