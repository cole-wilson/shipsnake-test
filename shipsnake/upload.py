import os
import sys
import toml

def main(arguments,ids):
	if not os.path.isfile('.'+os.sep+'shipsnake.toml'):
		print('Please create a config file with `shipsnake wizard` first.')
		sys.exit(0)
	with open('.'+os.sep+'shipsnake.toml') as datafile:
		data = toml.loads(datafile.read())
	version = data['latest_build']
	if "pypi" in ids or len(ids)==1:
		print("Please make sure that you have a https://pypi.org/ account.")
		try:
			import twine
		except:
			input('Press enter to continue installing `twine`. Press ctrl+c to exit.')
			os.system('python3 -m pip install --user --upgrade twine || python3 -m pip install --upgrade twine')
			import twine
		del twine
		os.system('python3 -m twine upload dist'+os.sep+'pypi'+os.sep+'*')
	if "github" in ids or len(ids)==1:
		f = f'git config user.name "{data["author"]}";git config user.email "{data["email"]}";git add .;git tag v{version};git commit -m "Release v{version}";git remote add origin https://github.com/{data["build"]["github"]}.git || echo;git push -u origin master --tags;'
		os.system(f)