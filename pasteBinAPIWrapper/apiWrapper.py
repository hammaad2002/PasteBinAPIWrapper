import requests
from typing import Optional

class wrapper(object):
    '''
    PasteBin's API for Python users. It can perform the following tasks on 
    Pastebin:

    1) Create a new paste.

    2) List all the pastes.

    3) Delete a specific paste.

    4) Get users' information and settings.

    5) Get the raw output of a user's paste (including private pastes).

    6) Get the raw output of any public or unlisted paste on Pastebin.
    '''

    def __init__(self, api_user_name: str, api_user_password: str, api_dev_key: str)-> None:
        
        '''
        Initialization method of this class, which will initialize all the 
        necessary components needed to perform further tasks. This includes 
        obtaining the user's 'api_user_key,' which is required for most tasks.

        Args:

        api_user_name : Username of your Pastebin ID.
        Type : str

        api_user_password: Password of your Pastebin ID.
        Type: str

        api_dev_key: Developer Key of your account given by Pastebin, 
                               which can be accessed on this webpage 
                               'https://pastebin.com/doc_api#1'.
        Type: str

        Returns:
        None: Since this is the 'init' method.
        '''

        self.urls = ["https://pastebin.com/api/api_login.php", 
                     "https://pastebin.com/api/api_post.php"]

        self.api_dev_key = api_dev_key

        # Prepare the data to be sent in the POST request
        data = {
            "api_dev_key": api_dev_key,
            "api_user_name": api_user_name,
            "api_user_password": api_user_password,
        }

        # Make the POST request
        response = requests.post(self.urls[0], data=data)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            self.api_user_key = response.text

        else:
            print(f"Request failed with status code {response.status_code}")
    
    def get_api_user_key(self)-> str:
        '''
        Getter method to get the 'api_user_key' of the user if they need it.

        Returns:
        str: The user's 'api_user_key' is returned.

        '''
        return self.api_user_key

    def create_paste(self, api_paste_code: str, use_api_user_key: bool=True, 
                         api_paste_name: Optional[str]=None, 
                         api_paste_format: Optional[str]=None, 
                         api_paste_private: Optional[str]=None, 
                         api_paste_expire_date: Optional[str]=None, 
                         api_folder_key: Optional[str]=None)-> str:
        '''
        This method will create a paste in the user's ID.

        Args:

        api_paste_code: The main text that will be in the newly created paste of
                        the user.
        Type: str

        use_api_user_key: If the user wants to use 'api_user_key' for creating 
                          this new paste. If not used, then this will create a 
                          guest paste. If allowed, you will have the option of 
                          whether you want to create this paste as private, 
                          unlisted, or public.
        Type: bool

        api_paste_name: An optional argument if the user wants to name their 
                        paste's file. If no argument is passed, the default name
                        'Untitled' is assigned by Pastebin to the file.
        Type: Optional[str]

        api_paste_format: An optional argument if the user wants to specify the 
                          paste's format, for example, whether it is 'C++' code 
                          or 'Python' code or some other type.
        Type: Optional[str]

        api_paste_private: An optional argument if the user wants to specify 
                           their paste's privacy. If no argument is provided, 
                           then by default, Pastebin will make it public.
        Type: Optional[str]

        api_paste_expire_date: An optional argument if the user wants to specify
                               their paste's expiry date. If no argument is 
                               given, then by default, Pastebin will make it a 
                               permanent paste or a paste with no expiry.
        Type: Optional[str]

        api_folder_key: An optional argument if the user wants to specify their 
                        paste to be stored in a specific folder. To find the 
                        code of your folder that is to be passed over here, you 
                        need to navigate to the folder through your ID yourself 
                        first as there is no way to retrieve it using the 
                        developer's provided API. An example of it is 
                        'https://pastebin.com/u/haste_69/1/Pvpcw9JW'.So in this 
                        link, 'Pvpcw9JW' is the folder's code that is to be 
                        passed to this argument.
        Type: Optional[str]

        Returns:
        str: Returns the link of the newly created paste. An example of it is
             'https://pastebin.com/79AaHSEh'.
        '''
      
        new_temp_one = ['4cs',
        '6502acme',
        '6502kickass',
        '6502tasm',
        'abap',
        'actionscript',
        'actionscript3',
        'ada',
        'aimms',
        'algol68',
        'apache',
        'applescript',
        'apt_sources',
        'arduino',
        'arm',
        'asm',
        'asp',
        'asymptote',
        'autoconf',
        'autohotkey',
        'autoit',
        'avisynth',
        'awk',
        'bascomavr',
        'bash',
        'basic4gl',
        'dos',
        'bibtex',
        'b3d',
        'blitzbasic',
        'bmx',
        'bnf',
        'boo',
        'bf',
        'c',
        'csharp',
        'c_winapi',
        'cpp',
        'cpp-winapi',
        'cpp-qt',
        'c_loadrunner',
        'caddcl',
        'cadlisp',
        'ceylon',
        'cfdg',
        'c_mac',
        'chaiscript',
        'chapel',
        'cil',
        'clojure',
        'klonec',
        'klonecpp',
        'cmake',
        'cobol',
        'coffeescript',
        'cfm',
        'css',
        'cuesheet',
        'd',
        'dart',
        'dcl',
        'dcpu16',
        'dcs',
        'delphi',
        'oxygene',
        'diff',
        'div',
        'dot',
        'e',
        'ezt',
        'ecmascript',
        'eiffel',
        'email',
        'epc',
        'erlang',
        'euphoria',
        'fsharp',
        'falcon',
        'filemaker',
        'fo',
        'f1',
        'fortran',
        'freebasic',
        'freeswitch',
        'gambas',
        'gml',
        'gdb',
        'gdscript',
        'genero',
        'genie',
        'gettext',
        'go',
        'godot-glsl',
        'groovy',
        'gwbasic',
        'haskell',
        'haxe',
        'hicest',
        'hq9plus',
        'html4strict',
        'html5',
        'icon',
        'idl',
        'ini',
        'inno',
        'intercal',
        'io',
        'ispfpanel',
        'j',
        'java',
        'java5',
        'javascript',
        'jcl',
        'jquery',
        'json',
        'julia',
        'kixtart',
        'kotlin',
        'ksp',
        'latex',
        'ldif',
        'lb',
        'lsl2',
        'lisp',
        'llvm',
        'locobasic',
        'logtalk',
        'lolcode',
        'lotusformulas',
        'lotusscript',
        'lscript',
        'lua',
        'm68k',
        'magiksf',
        'make',
        'mapbasic',
        'markdown',
        'matlab',
        'mercury',
        'metapost',
        'mirc',
        'mmix',
        'mk-61',
        'modula2',
        'modula3',
        '68000devpac',
        'mpasm',
        'mxml',
        'mysql',
        'nagios',
        'netrexx',
        'newlisp',
        'nginx',
        'nim',
        'nsis',
        'oberon2',
        'objeck',
        'objc',
        'ocaml',
        'ocaml-brief',
        'octave',
        'pf',
        'glsl',
        'oorexx',
        'oobas',
        'oracle8',
        'oracle11',
        'oz',
        'parasail',
        'parigp',
        'pascal',
        'pawn',
        'pcre',
        'per',
        'perl',
        'perl6',
        'phix',
        'php',
        'php-brief',
        'pic16',
        'pike',
        'pixelbender',
        'pli',
        'plsql',
        'postgresql',
        'postscript',
        'povray',
        'powerbuilder',
        'powershell',
        'proftpd',
        'progress',
        'prolog',
        'properties',
        'providex',
        'puppet',
        'purebasic',
        'pycon',
        'python',
        'pys60',
        'q',
        'qbasic',
        'qml',
        'rsplus',
        'racket',
        'rails',
        'rbs',
        'rebol',
        'reg',
        'rexx',
        'robots',
        'roff',
        'rpmspec',
        'ruby',
        'gnuplot',
        'rust',
        'sas',
        'scala',
        'scheme',
        'scilab',
        'scl',
        'sdlbasic',
        'smalltalk',
        'smarty',
        'spark',
        'sparql',
        'sqf',
        'sql',
        'sshconfig',
        'standardml',
        'stonescript',
        'sclang',
        'swift',
        'systemverilog',
        'tsql',
        'tcl',
        'teraterm',
        'texgraph',
        'thinbasic',
        'typescript',
        'typoscript',
        'unicon',
        'uscript',
        'upc',
        'urbi',
        'vala',
        'vbnet',
        'vbscript',
        'vedit',
        'verilog',
        'vhdl',
        'vim',
        'vb',
        'visualfoxpro',
        'visualprolog',
        'whitespace',
        'whois',
        'winbatch',
        'xbasic',
        'xml',
        'xojo',
        'xorg_conf',
        'xpp',
        'yaml',
        'yara',
        'z80',
        'zxbasic']
        new_temp_two = ["0", "1", "2"]
        new_temp_three = ["N", "10M", "1H", "1D", "1W", "2W", "1M", "6M", "1Y"]
    
        # Define the API endpoint and parameters [Required Parameters]
        api_url = self.urls[1]
        api_option = "paste" # Because I am creating a new paste so this will be constant for this job

        # [Optional Parameters]
        if use_api_user_key == True:
            api_user_key = self.api_user_key
        elif use_api_user_key == False:
            api_user_key = None
        if api_paste_name is not None:
            api_paste_name = api_paste_name
        if api_paste_format is not None and api_paste_format in new_temp_one:
            api_paste_format = api_paste_format
        if api_paste_private is not None and api_paste_private in new_temp_two:
            api_paste_private = api_paste_private
        if api_paste_expire_date is not None and api_paste_expire_date in new_temp_three:
            api_paste_expire_date = api_paste_expire_date
        if api_folder_key is not None:
            api_folder_key = api_folder_key
        
        # Prepare the data to be sent in the POST request
        data = {
            "api_dev_key": self.api_dev_key,
            "api_paste_code": api_paste_code,
            "api_option": api_option,
            "api_user_key": api_user_key,
            "api_paste_name": api_paste_name,
            "api_paste_format": api_paste_format,
            "api_paste_private": api_paste_private,
            "api_paste_expire_date": api_paste_expire_date,
            "api_folder_key": api_folder_key,
        }
        
        # Make the POST request
        response = requests.post(api_url, data=data)
        
        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            new_paste_link = response.text
            return new_paste_link

        else:
            print(f"Request failed with status code {response.status_code}")

    def list_all_paste(self, api_results_limit: int = 100)-> str:
        '''
        This method is used to list all the pastes stored in the user's ID.

        Args:

        api_results_limit: The limit of results to return in one go. By default,
                           this value is set to 100 as provided by Pastebin's 
                           developers.
        Type: int

        Returns:
        str: Returns the list of pastes as a single string.
        '''

        # Define the API endpoint and parameters
        api_url = self.urls[1] 
        api_option = "list"

        # Prepare the data to be sent in the POST request
        data = {
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.api_user_key,
            "api_option": api_option,
            "api_results_limit": api_results_limit,
        }

        # Make the POST request
        response = requests.post(api_url, data=data)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            all_user_paste = response.text
            return all_user_paste

        else:
            print(f"Request failed with status code {response.status_code}")

    def delete_paste(self, api_paste_key: str)-> str:
        '''
        This method will delete a specific user's paste stored in their ID.

        Args:

        api_paste_key: This is the unique key of the particular paste that needs
                       to be passed here in order to delete it specifically.
        Type: str

        Returns:
        str: A string saying 'Paste Removed' if everything goes well.
        '''

        # Define the API endpoint and parameters
        api_url = self.urls[1]
        api_option = "delete"

        # Prepare the data to be sent in the POST request
        data = {
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.api_user_key,
            "api_option": api_option,
            "api_paste_key": api_paste_key,
        }

        # Make the POST request
        response = requests.post(api_url, data=data)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            delete_response = response.text
            return delete_response

        else:
            print(f"Request failed with status code {response.status_code}")

    def user_info_and_settings(self)-> str:
        '''
        This is a kind of getter method that returns all the user's information 
        and settings for their ID.

        Returns:
        str: All the user's settings and information are returned.
        '''

        # Define the API endpoint and parameters
        api_url = self.urls[1]
        api_option = "userdetails"

        # Prepare the data to be sent in the POST request
        data = {
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.api_user_key,
            "api_option": api_option,
        }

        # Make the POST request
        response = requests.post(api_url, data=data)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            user_info_response = response.text
            return user_info_response

        else:
            print(f"Request failed with status code {response.status_code}")
    
    def get_raw_paste_output(self, api_paste_key: str)-> str:
        '''
        This method is used to retrieve content from a specific user's paste 
        (including private pastes, in addition to public and unlisted ones).

        Args:

        api_paste_key: This is the unique key of the particular paste that needs
                       to be passed here in order to retrieve its content.
        Type: str

        Returns:
        str: Content stored inside the particular paste.
        '''

        # Define the API endpoint and parameters
        api_url = self.urls[1]
        api_option = "show_paste"

        # Prepare the data to be sent in the POST request
        data = {
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.api_user_key,
            "api_option": api_option,
            "api_paste_key": api_paste_key,
        }

        # Make the POST request
        response = requests.post(api_url, data=data)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            raw_paste_output = response.text
            return raw_paste_output

        else:
            print(f"Request failed with status code {response.status_code}")

    def get_raw_paste_any(self, api_paste_key: str):
        '''
        This method is used to extract or retrieve the content of any public or
        unlisted paste available on Pastebin.

        Args:

        api_paste_key: You can either pass the whole link of the paste
                       or just the key of the paste; it's your choice.
        Type: str

        Returns:
        str: Content stored inside the particular paste.
        '''

        # Define the API endpoint and parameters
        arg = api_paste_key
        if arg.find('pastebin.com') != -1:
            for i in range(len(arg)-1, 0, -1):
                if arg[i] == '/':
                    break
            link = 'https://pastebin.com/raw/' + arg[20+1:]

            # Returning the content of the paste
            return requests.get(link).text
        else:
            link = 'https://pastebin.com/raw/' + api_paste_key
            
            # Returning the content of the paste
            return requests.get(link).text