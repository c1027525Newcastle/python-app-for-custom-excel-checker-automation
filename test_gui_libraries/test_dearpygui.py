# import dearpygui.dearpygui as dpg

# dpg.create_context()
# dpg.create_viewport(title='Custom Title', width=600, height=300)

# with dpg.window(label="Example Window"):
#     dpg.add_text("Hello, world")
#     dpg.add_button(label="Save")
#     dpg.add_input_text(label="string", default_value="Quick brown fox")
#     dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

"""
This is a simple test script for DearPyGui. (It's the official example from the DearPyGui documentation.)
"""
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()