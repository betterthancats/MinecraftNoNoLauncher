import minecraftsession
import subprocess
import os

minecraftUsername = 'betterthancats'
minecraftPassword = 'maru1337'
minecraftHome = 'C:/Users/cat/Desktop/box'
minecraftDir = minecraftHome + '/.minecraft'
minecraftVersion = 'btw' 
javaExe = 'C:/Program Files/Java/jdk1.7.0_51/bin/javaw.exe'
javaOpts = '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xms2G -Xmx2G'




# get minecraft session
mcsession = minecraftsession.MinecraftSession()
if not mcsession.login(minecraftUsername, minecraftPassword, 'something random'):
  print 'Wrong email or password'
minecraftSessionId = mcsession.getSession()

# copy win env
minecraftEnv = dict(os.environ)
# change win env %APPDATA%
minecraftEnv['APPDATA'] = minecraftHome

# start minecraft (the arguments are only valid for minecraft 1.5.2 / better than wolves)
subprocess.Popen([
javaExe,
javaOpts,
r"-Djava.library.path=" + minecraftDir + "/versions/" + minecraftVersion + "/" + minecraftVersion + "-natives",
r"-cp",
minecraftDir + r"\libraries\net\minecraft\launchwrapper\1.5\launchwrapper-1.5.jar;" + 
  minecraftDir + r"\libraries\net\sf\jopt-simple\jopt-simple\4.5\jopt-simple-4.5.jar;" + 
  minecraftDir + r"\libraries\org\ow2\asm\asm-all\4.1\asm-all-4.1.jar;" + 
  minecraftDir + r"\libraries\net\java\jinput\jinput\2.0.5\jinput-2.0.5.jar;" + 
  minecraftDir + r"\libraries\net\java\jutils\jutils\1.0.0\jutils-1.0.0.jar;" + 
  minecraftDir + r"\libraries\org\lwjgl\lwjgl\lwjgl\2.9.0\lwjgl-2.9.0.jar;" + 
  minecraftDir + r"\libraries\org\lwjgl\lwjgl\lwjgl_util\2.9.0\lwjgl_util-2.9.0.jar;" + 
  minecraftDir + "/versions/" + minecraftVersion + "/" + minecraftVersion + ".jar",
r"net.minecraft.launchwrapper.Launch",
minecraftUsername,
minecraftSessionId,
r"--gameDir",
minecraftDir, 
r"--assetsDir",
minecraftDir + r"\assets\virtual\legacy"],
cwd=minecraftDir, shell=True, env=minecraftEnv, stdout=subprocess.PIPE).communicate()
