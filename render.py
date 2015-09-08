imgs = (
{'name': 'ic_action_achievement',       'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_add',               'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_alarm',             'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_amazon',            'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_anchor',            'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_android',           'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_armchair',          'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_arrow_bottom',      'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_arrow_left_bottom', 'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_arrow_left',        'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0},
{'name': 'ic_action_arrow_left_top',    'h': 32, 'w': 32, 'offset_x': 0, 'offset_y': 0})



from jinja2 import Template

template_css = Template(open('./template.css').read())
rendered = template_css.render(imgs = imgs, sprite = {'name': 'sprite.png'}, program = {'name': 'SpritePy', 'version': '0.0.1'})

sprite_css = open('sprite.css', 'w')
sprite_css.write(rendered)
sprite_css.close()


template_html = Template(open('./template.html').read())
rendered = template_html.render(imgs = imgs, sprite = {'name': 'sprite.png'}, program = {'name': 'SpritePy', 'version': '0.0.1'})

sprite_html = open('sprite.html', 'w')
sprite_html.write(rendered)
sprite_html.close()
