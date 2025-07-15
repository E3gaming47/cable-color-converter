from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp

class TelephoneCableColorCode:
    def __init__(self):
        self.tip_colors = ["White", "Red", "Black", "Yellow", "Violet"]
        self.ring_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
        
        self.pairs = []
        for tip in self.tip_colors:
            for ring in self.ring_colors:
                self.pairs.append((tip, ring))
    
    def number_to_colors(self, pair_number):
        if pair_number < 1 or pair_number > 25:
            return None, None, "Error: Pair number must be between 1 and 25"
        
        tip, ring = self.pairs[pair_number - 1]
        return tip, ring, None
    
    def colors_to_number(self, tip_color, ring_color):
        tip_color = tip_color.strip().capitalize()
        ring_color = ring_color.strip().capitalize()
        
        try:
            pair_index = self.pairs.index((tip_color, ring_color))
            return pair_index + 1, None
        except ValueError:
            return None, f"Error: Invalid color combination '{tip_color}-{ring_color}'"

class CableColorApp(App):
    def build(self):
        self.cable = TelephoneCableColorCode()
        self.title = "Cable Color Converter"
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Title
        title = Label(text='Cable Color Code Converter', 
                     font_size=dp(24), 
                     size_hint_y=None, 
                     height=dp(60),
                     color=(1, 1, 1, 1))
        main_layout.add_widget(title)
        
        # Tab buttons
        tab_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50), spacing=dp(10))
        
        self.tab1_btn = Button(text='Number → Colors', 
                              background_color=(0.13, 0.59, 0.95, 1),
                              font_size=dp(16))
        self.tab1_btn.bind(on_press=self.show_number_to_colors)
        
        self.tab2_btn = Button(text='Colors → Number', 
                              background_color=(0.26, 0.26, 0.26, 1),
                              font_size=dp(16))
        self.tab2_btn.bind(on_press=self.show_colors_to_number)
        
        tab_layout.add_widget(self.tab1_btn)
        tab_layout.add_widget(self.tab2_btn)
        main_layout.add_widget(tab_layout)
        
        # Content area
        self.content_layout = BoxLayout(orientation='vertical', spacing=dp(15))
        main_layout.add_widget(self.content_layout)
        
        # Reference button
        ref_btn = Button(text='📋 View All Pairs', 
                        background_color=(1, 0.6, 0, 1),
                        size_hint_y=None, 
                        height=dp(50),
                        font_size=dp(16))
        ref_btn.bind(on_press=self.show_reference)
        main_layout.add_widget(ref_btn)
        
        # Show default tab
        self.show_number_to_colors(None)
        
        return main_layout
    
    def clear_content(self):
        self.content_layout.clear_widgets()
    
    def show_number_to_colors(self, instance):
        self.tab1_btn.background_color = (0.13, 0.59, 0.95, 1)
        self.tab2_btn.background_color = (0.26, 0.26, 0.26, 1)
        
        self.clear_content()
        
        # Input section
        input_label = Label(text='Enter Pair Number (1-25):', 
                           font_size=dp(18), 
                           size_hint_y=None, 
                           height=dp(40))
        self.content_layout.add_widget(input_label)
        
        self.number_input = TextInput(multiline=False, 
                                     font_size=dp(18), 
                                     size_hint_y=None, 
                                     height=dp(50),
                                     input_filter='int')
        self.content_layout.add_widget(self.number_input)
        
        convert_btn = Button(text='Convert', 
                            background_color=(0.3, 0.69, 0.31, 1),
                            size_hint_y=None, 
                            height=dp(50),
                            font_size=dp(16))
        convert_btn.bind(on_press=self.convert_number_to_colors)
        self.content_layout.add_widget(convert_btn)
        
        # Result
        self.result_label1 = Label(text='Enter a number to see colors', 
                                  font_size=dp(16), 
                                  size_hint_y=None, 
                                  height=dp(60))
        self.content_layout.add_widget(self.result_label1)
    
    def show_colors_to_number(self, instance):
        self.tab1_btn.background_color = (0.26, 0.26, 0.26, 1)
        self.tab2_btn.background_color = (0.13, 0.59, 0.95, 1)
        
        self.clear_content()
        
        # Tip color
        tip_label = Label(text='Tip Color (Primary):', 
                         font_size=dp(18), 
                         size_hint_y=None, 
                         height=dp(40))
        self.content_layout.add_widget(tip_label)
        
        self.tip_spinner = Spinner(text='Select Tip Color',
                                  values=self.cable.tip_colors,
                                  size_hint_y=None,
                                  height=dp(50),
                                  font_size=dp(16))
        self.content_layout.add_widget(self.tip_spinner)
        
        # Ring color
        ring_label = Label(text='Ring Color (Secondary):', 
                          font_size=dp(18), 
                          size_hint_y=None, 
                          height=dp(40))
        self.content_layout.add_widget(ring_label)
        
        self.ring_spinner = Spinner(text='Select Ring Color',
                                   values=self.cable.ring_colors,
                                   size_hint_y=None,
                                   height=dp(50),
                                   font_size=dp(16))
        self.content_layout.add_widget(self.ring_spinner)
        
        convert_btn = Button(text='Convert', 
                            background_color=(0.3, 0.69, 0.31, 1),
                            size_hint_y=None, 
                            height=dp(50),
                            font_size=dp(16))
        convert_btn.bind(on_press=self.convert_colors_to_number)
        self.content_layout.add_widget(convert_btn)
        
        # Result
        self.result_label2 = Label(text='Select colors to see pair number', 
                                  font_size=dp(16), 
                                  size_hint_y=None, 
                                  height=dp(60))
        self.content_layout.add_widget(self.result_label2)
    
    def convert_number_to_colors(self, instance):
        try:
            pair_num = int(self.number_input.text)
            tip, ring, error = self.cable.number_to_colors(pair_num)
            
            if error:
                self.result_label1.text = error
                self.result_label1.color = (0.96, 0.26, 0.21, 1)
            else:
                self.result_label1.text = f"Pair {pair_num}: {tip} - {ring}"
                self.result_label1.color = (0.3, 0.69, 0.31, 1)
        except ValueError:
            self.result_label1.text = "Please enter a valid number"
            self.result_label1.color = (0.96, 0.26, 0.21, 1)
    
    def convert_colors_to_number(self, instance):
        tip_color = self.tip_spinner.text
        ring_color = self.ring_spinner.text
        
        if tip_color == 'Select Tip Color' or ring_color == 'Select Ring Color':
            self.result_label2.text = "Please select both colors"
            self.result_label2.color = (0.96, 0.26, 0.21, 1)
            return
        
        pair_num, error = self.cable.colors_to_number(tip_color, ring_color)
        
        if error:
            self.result_label2.text = error
            self.result_label2.color = (0.96, 0.26, 0.21, 1)
        else:
            self.result_label2.text = f"{tip_color} - {ring_color}: Pair {pair_num}"
            self.result_label2.color = (0.3, 0.69, 0.31, 1)
    
    def show_reference(self, instance):
        # Create popup with scrollable content
        content = BoxLayout(orientation='vertical', spacing=dp(5))
        
        # Header
        header = GridLayout(cols=3, size_hint_y=None, height=dp(40))
        header.add_widget(Label(text='Pair #', font_size=dp(14), bold=True))
        header.add_widget(Label(text='Tip Color', font_size=dp(14), bold=True))
        header.add_widget(Label(text='Ring Color', font_size=dp(14), bold=True))
        content.add_widget(header)
        
        # Pairs list
        pairs_layout = GridLayout(cols=3, spacing=dp(2), size_hint_y=None)
        pairs_layout.bind(minimum_height=pairs_layout.setter('height'))
        
        for i, (tip, ring) in enumerate(self.cable.pairs, 1):
            pairs_layout.add_widget(Label(text=str(i), font_size=dp(12), size_hint_y=None, height=dp(30)))
            pairs_layout.add_widget(Label(text=tip, font_size=dp(12), size_hint_y=None, height=dp(30)))
            pairs_layout.add_widget(Label(text=ring, font_size=dp(12), size_hint_y=None, height=dp(30)))
        
        scroll = ScrollView()
        scroll.add_widget(pairs_layout)
        content.add_widget(scroll)
        
        popup = Popup(title='25-Pair Color Reference',
                      content=content,
                      size_hint=(0.8, 0.8))
        popup.open()

if __name__ == '__main__':
    CableColorApp().run()