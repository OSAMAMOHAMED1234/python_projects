import os
class Template:
  template_name = ''
  context = None

  def __init__(self, template_name='', context=None, *args, **kwargs):
    self.template_name = template_name
    self.context = context

  def get_template(self):
    template_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'), self.template_name)
    if not os.path.exists(template_path):
      raise Exception(f'This path does not exist : {template_path}')
    template_string = ''
    with open(template_path, 'r') as f:
      template_string = f.read()
    return template_string

  def render(self, context=None):
    render_ctx = context
    if self.context != None:
      render_ctx = self.context
    if not isinstance(render_ctx, dict):
      render_ctx = {}
    template_string = self.get_template()
    return template_string.format(**render_ctx)


obj = Template(template_name='test.html', context={'name': 'OSAMA'})
print(obj.render())
obj.context= None
print(obj.render(context={'name': 'os'}))


obj2 = Template(template_name='test.html')
print(obj2.render(context={'name': 'os'}))