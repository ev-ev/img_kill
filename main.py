import os,sys

class repeatExtensionError(Exception):
	def __init__(self,ext):
		self.message='You have attempted to use the same file extension more than once: '+ext
	def __str__(self):
		return self.message
    

def main():
	storage_name=os.path.abspath('./overwrite_data')
	self_name=os.path.abspath(sys.argv[0])
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
	dir=os.walk('.')
	requires_assistance={}
	for root, dirs, files in dir:
		for file in files:
			if os.path.abspath(root+'/'+file)==self_name or os.path.abspath(root)==storage_name:
				continue
			file_arr=file.split('.')
			if len(file_arr)!=2:
				continue
			if file_arr[1] in over_exts:
				requires_assistance[root+'/'+file]=over_paths[over_exts.index(file_arr[1])]
	
	for assist in requires_assistance:
		file=open(requires_assistance[assist],'rb')
		data=file.read()
		file.close()
		file=open(assist,'wb')
		file.write(data)
		file.close
	
if __name__=="__main__":
	main()