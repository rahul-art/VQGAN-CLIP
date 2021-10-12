curl -L -o vqgan_imagenet_f16_16384.yaml -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1' #ImageNet 16384
curl -L -o vqgan_imagenet_f16_16384.ckpt -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1' #ImageNet 16384
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
