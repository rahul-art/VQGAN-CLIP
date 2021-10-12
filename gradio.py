import subprocess
subprocess.call("download_models.sh")
git clone 'https://github.com/openai/CLIP'
git clone 'https://github.com/CompVis/taming-transformers'
import gradio as gr 
def outbreak_forecast(Practice):
  python generate.py -p f"{Practice}"
  return "output.png"

Practice = gr.inputs.Textbox()
output = gr.outputs.Image()

iface = gr.Interface(fn=outbreak_forecast,
    inputs=[Practice], outputs=output)#
iface.launch(debug=True)
