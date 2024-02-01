# diffusiondb
n_imgs = 100000
batch_size = 1000

# common
n_search = 40
n_compress = 0.2
n_test = 5

# stable diffusion
model_id = "CompVis/stable-diffusion-v1-4"
sd_height = 512
sd_width = 512
n_inference_steps = 50
n_images_per_prompt = 2
# n_epo = 1 # one epo cost 20s
n_device = 1 # number of GPU
sd_ip = 'http://127.0.0.1:'
rand_left = 212463292853
rand_right = 958446223563

# My config
numberOfGeneration = 10
epo = numberOfGeneration / (n_device * n_images_per_prompt)
device_id = 1
scale_left = 6
scale_right = 8
prompt = "A surreal landscape with vibrant colors and unusual shapes."
negative_prompt = ""

