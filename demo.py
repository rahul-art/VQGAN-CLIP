import subprocess
subprocess.call(["chmod", "+x", "download_models.sh"]) 
import os
os.system("sh download_models.sh") 
#subprocess.run("VQGAN-CLIP/download_models.sh")
subprocess.call(['git', 'clone', "https://github.com/openai/CLIP"])
subprocess.call(['git', 'clone', "https://github.com/CompVis/taming-transformers"])
import gradio as gr 
def outbreak_forecast(Practice):
  subprocess.call(["python", "generate.py","-p", f"{Practice}","-i", "50"])
  return "output.png"


iface = gr.Interface(fn=outbreak_forecast,inputs="text",outputs= 'image')#
iface.launch(debug=True)
