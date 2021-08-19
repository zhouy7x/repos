import sys
import os

cmd = sys.argv[1] if sys.argv[1:] else "makebox"
name = sys.argv[2] if sys.argv[2:] else "lan1"
lan = sys.argv[3] if sys.argv[3:] else ""
psm = sys.argv[4] if sys.argv[4:] else ""


def func(cmd, name, lan, psm):
    cmd_list = ['makebox', 'train', 'debug']
    if cmd not in cmd_list:
        print("ERROR: Must give cmd in %s!"%str(cmd_list))
        return
    if cmd == 'makebox':
        exp = 0
        # for i in range(10):
        #     if os.path.exists("%s.test.exp%d.tif"%(name, i)):
        #         exp += 1
        #     else:
        #         break
        cmd_string = "tesseract %s.test.exp%d.tif %s.test.exp%d" % (name, exp, name, exp)
        if lan:
            cmd_string += " -l %s" % lan
        if psm:
            cmd_string += " --psm %s" % psm
        cmd_string += " batch.nochop makebox"
        print(cmd_string)
        os.system(cmd_string)
        return
    elif cmd == 'debug':
        with open('font_properties', 'w') as f:
            f.write("test 0 0 0 0 0")
        cmd_string1 = "tesseract %s.test.exp0.tif %s.test.exp0 nobatch box.train" % (name, name)
        print(cmd_string1)
        os.system(cmd_string1)
        return
    elif cmd == 'train':
        with open('font_properties', 'w') as f:
            f.write("test 0 0 0 0 0")
        cmd_string1 = "tesseract %s.test.exp0.tif %s.test.exp0 nobatch box.train" % (name, name)
        cmd_string2 = "unicharset_extractor %s.test.exp0.box" % name
        cmd_string3 = "shapeclustering -F font_properties -U unicharset -O %s.unicharset %s.test.exp0.tr" % (name, name)
        cmd_string4 = "mftraining -F font_properties -U unicharset -O %s.unicharset %s.test.exp0.tr" % (name, name)
        cmd_string5 = "cntraining %s.test.exp0.tr" % name
        print(cmd_string1)
        os.system(cmd_string1)
        print(cmd_string2)
        os.system(cmd_string2)
        print(cmd_string3)
        os.system(cmd_string3)
        print(cmd_string4)
        os.system(cmd_string4)
        print(cmd_string5)
        os.system(cmd_string5)
        print("Rename 'inttemp' to '%s.inttemp'"%name)
        os.remove('%s.inttemp'%name)
        os.rename('inttemp', '%s.inttemp'%name)
        print("Rename 'pffmtable' to '%s.pffmtable'"%name)
        os.remove('%s.pffmtable'%name)
        os.rename('pffmtable', '%s.pffmtable'%name)
        print("Rename 'shapetable' to '%s.shapetable'"%name)
        os.remove('%s.shapetable'%name)
        os.rename('shapetable', '%s.shapetable'%name)
        print("Rename 'normproto' to '%s.normproto'"%name)
        os.remove('%s.normproto'%name)
        os.rename('normproto', '%s.normproto'%name)
        cmd_string6 = "combine_tessdata %s."%name
        print(cmd_string6)
        os.system(cmd_string6)
        print("Output file is: %s.traineddata"%name)
        return

func(cmd, name, lan, psm)
        