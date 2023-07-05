from utils import encode_image

def generate_payload(previous_frame:str, current_frame:str, next_frame:str, width:int, height:int):
	payload = {
		'init_images' : [ encode_image(current_frame) ],
		'resize_mode' : 0,
		'denoising_strength' : 0.32,
		'prompt' : "(masterpiece, best quality)",
		'negative_prompt' : "(low quality, worst quality:1.2), EasyNegative, EasyNegativeV2",
		'seed' : 45510,
		'sampler_name' : "Euler a",
		'sampler_index' : "euler",
		'batch_size' : 1,
		'steps' : 10,
		'cfg_scale' : 6.4,
		'width' : width,
		'height' : height,
		'alwayson_scripts' : {
			'ControlNet' : {
				'args' : [
					{          
						'enabled': True,
						'input_image': encode_image(previous_frame),
						'module': "reference_only",
						'weight': 1.0,
						'threshold_a': 0.5
					},
					{          
						'enabled': True,
						'input_image': encode_image(next_frame),
						'module': "reference_only",
						'weight': 1.0,
						'threshold_a': 0.5
					}
				]
			}
		}
	}

	return payload