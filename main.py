import os

class repeatExtensionError(Exception):
	def __init__(self,ext):
		self.message='You have attempted to use the same file extension more than once: '+ext
	def __str__(self):
		return self.message
    

def main():
	storage_name='./overwrite_data'
	over_paths=[]
	over_exts=[]
	dir=os.walk(storage_name)

	for root, dirs, files in dir:
		for file in files:
			file_arr=file.split('.')
			over_paths.append(root+'/'+file)
			over_exts.append(file_arr[1])

	seen_exts=[]

	for ext in over_exts:
		if ext not in seen_exts:
			seen_exts.append(ext)
		else:
			raise repeatExtensionError('.'+ext)
	print(over_paths)
	dir=os.walk('.')
	requires_assistance={}
	for root, dirs, files in dir:
		for file in files:
			file_arr=file
	
if __name__=="__main__":
	main()