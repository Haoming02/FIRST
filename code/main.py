from parameters import generate_payload
from utils import get_image_size
from utils import decode_image
import tkinter as tk
import requests
import os

def begin_process(sauce:str, output:str, port:int):
	if not os.path.exists(sauce):
		print(f'Invalid Source Path: {sauce}')
		return

	if not os.path.exists(output):
		print(f'Invalid Output Path: {output}')
		return

	if sauce == output:
		print('\n<!> Warning: Will override frames in place... <!>\n')

	print('Begin Processing...\n')
	print(f'\tRefine from:\t{sauce}')
	print(f'\tOutput to:\t{output}')
	print(f'\tAPI:\t\thttp://127.0.0.1:{port}/sdapi/v1/img2img')

	FILES = os.listdir(sauce)
	itrp_count = int(len(FILES) / 2)

	if len(FILES) < 3:
		print('\n========= ERROR ===========')
		print('Not enough frames detected!')
		print('===========================')
		return

	if len(FILES) % 2 == 0:
		print('\n=============================== ERROR ==================================')
		print('Even number of frames detected! This will throw error at the last frame!')
		print('========================================================================\n')

	print(f'\nNumber of Images to Process: {itrp_count}')

	width, height = get_image_size(sauce + '/' + FILES[0])

	for i in range(itrp_count):

		print(f'>\tProcessing {i} / {itrp_count}...')

		index = i * 2 + 1
		json = generate_payload(
			sauce + '/' + FILES[index - 1], 
			sauce + '/' + FILES[index], 
			sauce + '/' + FILES[index + 1], 
			width, height
		)						

		response = requests.post(url=f'http://127.0.0.1:{port}/sdapi/v1/img2img', json=json)		
		r = response.json()

		decode_image(r['images'][0], output + '/' + FILES[index])

	print('Process Done!')

def main():
	root = tk.Tk()
	root.title('F.I.R.S.T')
	root.geometry("320x240")

	mainWindow = tk.Frame(root, bg = "skyblue")
	mainWindow.pack(fill = "both", expand = 1)

	mainWindow.grid_rowconfigure(0, weight=1)
	mainWindow.grid_rowconfigure(1, weight=1)
	mainWindow.grid_rowconfigure(2, weight=1)
	mainWindow.grid_rowconfigure(3, weight=1)
	mainWindow.grid_columnconfigure(0, weight=1)
	mainWindow.grid_columnconfigure(1, weight=1)

	sauceTxt = tk.Label(mainWindow, text="Source Path:", fg = "lightcyan", bg = "skyblue")
	sauceTxt.grid(row=0, column=0, padx=8, pady=4)

	sauceEnt = tk.Entry(mainWindow)
	sauceEnt.grid(row=0, column=1, padx=4, pady=4)

	outputTxt = tk.Label(mainWindow, text="Output Path:", fg = "lightcyan", bg = "skyblue")
	outputTxt.grid(row=1, column=0, padx=8, pady=4)

	outputEnt = tk.Entry(mainWindow)
	outputEnt.grid(row=1, column=1, padx=4, pady=4)

	portTxt = tk.Label(mainWindow, text="Port:", fg = "lightcyan", bg = "skyblue")
	portTxt.grid(row=2, column=0, padx=8, pady=4)

	portEnt = tk.Entry(mainWindow)
	portEnt.grid(row=2, column=1, padx=4, pady=4)

	portEnt.insert(0, '7860')

	def run():
		begin_process(sauceEnt.get(), outputEnt.get(), portEnt.get())

	run_button = tk.Button(mainWindow, text="Run", command=run, fg = "lightcyan", bg = "deepskyblue")
	run_button.grid(row=3, columnspan = 2, sticky=tk.W+tk.E, padx=32, pady=8)

	root.resizable(False, False) 
	root.mainloop()

if __name__ == '__main__':
	main()