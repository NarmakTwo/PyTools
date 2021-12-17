class tools:
  def ginit(self):
    import colorama
    import os
  def __init__(self):
    self.ginit()
  def __init_subclass__(self):
    self.ginit()
  class file:
    def scan(file,string):
      """
      scan a file for a string
      """
      file1 = open(file, 'r')
      stringl = string.lower()
      if stringl in file1.read().lower():
        return True
      else:
        return False

    def append(file,string):
      """
      append to a file
      """
      with open(file,'a') as filea:
        filea.write(string)
    def overwrite(file,string):
      """
      overwrite a file
      """
      with open(file,'w') as filew:
        filew.write(string)
    def read(file):
      """
      read a file
      """
      with open(file,'r') as filer:
        return filer.read()
    def create(file):
      """
      create a file
      """
      open(file,'x')
    def check(file):
      """
      check if a file exists
      """
      try:
        if os.path.exists(file):
          return True
        elif not os.path.exists(file):
          return False
      except NameError:
        import os
        if os.path.exists(file):
          return True
        elif not os.path.exists(file):
          return False
    def delete(file):
      """
      delete a file
      """
      try:
        os.remove(file)
      except NameError:
        import os
        os.remove(file)
    def chdir(path):
      """
      change directory
      """
      try:
        os.chdir(path)
      except NameError:
        import os
        os.chdir(path)
    def lsdir(path):
      """
      list a directory
      """
      try:
        return os.listdir(path)
      except NameError:
        import os
        return os.listdir(path)
    def ls():
      """
      list current directory
      """
      try:
        return os.listdir(os.getcwd())
      except NameError:
        import os
        return os.listdir(os.getcwd())
  class string:
    def split(stringtosplit,stringtosplitby):
      """
      split a string into an array by a character inside the string
      """
      return str(stringtosplit).split(stringtosplitby)
    def chop(string):
      res = []
      for i in str(string):
        res.append(i)
      return res
    def listToString(listc):
      string = ''
      for i in listc:
        string = string + str(i)
      return string
    def string(inp):
      return str(inp)
  class console:
    def warn(text):
      print(colorama.Fore.RED + text + colorama.Fore.RESET)
    def comment(text):
      print(colorama.Style.DIM + text + colorama.Style.NORMAL)
    def print(text):
      print(text)
    def pcw(text):
      print(text)
      print(colorama.Style.DIM + text + colorama.Style.NORMAL)
      print(colorama.Fore.RED + text + colorama.Fore.RESET)
    def newline():
      print()
    def clear():
      os.system('clear')
    def wue(text):
      input(text)
