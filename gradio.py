import subprocess
subprocess.call(["chmod", "+x", "download_models.sh"]) 
subprocess.call(["download_models.sh"])
subprocess.call(['git', 'clone', "https://github.com/openai/CLIP"])
subprocess.call(['git', 'clone', "https://github.com/CompVis/taming-transformers"])
import gradio as gr 
def outbreak_forecast(Practice):
  subprocess.call(["python", "generate.py","-p", f"{Practice}","-i", 50])
  return "output.png"

Practice = gr.inputs.Textbox()
output = gr.outputs.Image()

iface = gr.Interface(fn=outbreak_forecast,
    inputs=[Practice], outputs=output)#
iface.launch(debug=True)
