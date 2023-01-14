def createFS(lines):
  fs = {}  # this will be our file system, a nested set of dicts {}
  current_directory_path = [
  ]  # this will be our file path, a list of dir names that act as nested 'keys' in fs

  # process each line in the input... our main execution loop!
  for line in lines:
    line = line.rstrip()

    # Handle cd command
    if line[0:4] == "$ cd":
      destination = line[5:]
      print("Command is cd and we are moving to \'" + destination + "\'")
      if destination == "/":
        current_directory_path = []
      elif destination == "..":
        current_directory_path.pop()
      else:
        current_directory_path.append(destination)
      continue

    # Handle ls command
    if line[0:4] == "$ ls":
      print("Command is ls")
      continue

    # I'm cheating a bit here by not explicitly tracking state, but
    # the only way to get to this codeblock is as the
    # subsequent output lines after ls command.

    # first establish a pointer into the file-system dict, starting at root
    working_folder = fs
    # then walk that pointer down the file-system dict, to current file path
    for p in current_directory_path:
      working_folder = working_folder[p]

    # now handle directories
    if line[0:3] == "dir":
      dir_name = line[4:]

      # we are going to  need to see if it exists in file system yet and add if not, make it
      if dir_name in working_folder:
        print("> found dir", dir_name, "that we already knew about")
      else:
        working_folder[dir_name] = {}  # create new sub dir
        print("> found dir", dir_name, "and created it in fs")

      # end of dir processing
      continue

    # now handle files
    file_size = line.split(" ")[0]
    file_name = line.split(" ")[1]

    # see if the file exists in file system yet and add if not, make it
    if file_name in working_folder:
      print("> found file", file_name, "that we already knew about")
    else:
      working_folder[file_name] = int(file_size)  # create new file
      print("> found file", file_name, "of size", file_size)

  # end of function
  return fs


#
# Simple function to kick off recursion and handle the global output
def solve(fs):
  global global_total, space_needed, dir_sizes
  global_total = 0
  space_needed = 30000000 - (70000000 - 40528671)  #hardcoding root size here
  dir_sizes = []

  depthFirstSolver(fs, "/")  # call our recursive loop starting at root
  print("Solution 1 is", global_total)
  print("Solution 2 is ", min(dir_sizes))


# Our recursive depth first counting function to go crawl these directories
def depthFirstSolver(current_dir, path):
  print("DFS on folder", path)
  global global_total, space_needed, dir_sizes
  current_dir_size = 0

  for k in current_dir:
    if type(current_dir[k]) is dict:  # it is a dir!
      current_dir_size += depthFirstSolver(
        current_dir[k], k)  # call on the subdir, recursively!
    else:  # it is a file
      current_dir_size += current_dir[k]  # add the file size to local total

  # add to running_total if not too big
  print("> the size of", path, "was: ", current_dir_size)
  if current_dir_size < 100000:
    global_total += current_dir_size

  # this bit is for solution 2, lets keep track of all eligible folder sizes once calculated
  if current_dir_size > space_needed:
    dir_sizes.append(current_dir_size)

  return current_dir_size  # for recursion loop


with open('input_bay.txt', 'r') as file:
  raw = file.readlines()
  fs = createFS(raw)
  solve(fs)
