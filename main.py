import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Team Manager')


with dpg.window(label="Recherche de joueur",no_close=True,height=500,width=1000):
    dpg.add_input_text(tag="Players",label="Entrez le nom du joueur")

    width, height, channels, data = dpg.load_image("Images.jpeg")
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

    with dpg.table(borders_innerV=True,borders_outerH=True):
        for i in range (0,5):
            dpg.add_table_column(label="")

    dpg.add_image("texture_tag",pos=(0,150))

    dpg.add_text("First name",parent="Texture_tag",pos=(250,150))
    dpg.add_text("Last Name",parent="Texture_tag",pos=(250,175))
    dpg.add_text("Numero de license",parent="Texture_tag",pos=(250,200))
    dpg.add_text("Adresse",parent="Texture_tag",pos=(250,225))

with dpg.window(label="Match",pos=(0,510),height=500,width=1000):
    dpg.add_input_text(label="Creer match(inserer le nom du match)",width=200);
    dpg.add_input_text(label="Ajouter un joueur pour ce match",width=200)
    

       




        
       

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()