from IPython.display import Image
def show_score():
  filename = ! ls *.png -Art | tail -n 1
  Image(filename=filename[0]) 
