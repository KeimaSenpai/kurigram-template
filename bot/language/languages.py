from typing import Dict
import json
import os

class LanguageManager:
    def __init__(self):
        self.languages: Dict[str, dict] = {}
        self.default_language = "en"
        self._load_languages()
    
    def _load_languages(self):
        """Carga todos los archivos de idioma desde el directorio languages"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        languages_dir = os.path.join(current_dir, "translations")
        
        # Check if languages directory exists
        if not os.path.exists(languages_dir):
            print(f"Warning: Languages directory not found at {languages_dir}")
            return
            
        for file in os.listdir(languages_dir):
            if file.endswith('.json'):
                language_code = file[:-5]  # Remove .json
                try:
                    with open(os.path.join(languages_dir, file), 'r', encoding='utf-8') as f:
                        self.languages[language_code] = json.load(f)
                        print(f"Loaded language: {language_code}")
                except Exception as e:
                    print(f"Error loading language {language_code}: {e}")
    
    def get_text(self, key: str, lang_code: str = None) -> str:
        """
        Obtiene el texto traducido para una clave específica
        """
        lang_code = lang_code or self.default_language
        
        # Si el idioma no existe, usar el idioma por defecto
        if lang_code not in self.languages:
            print(f"Language {lang_code} not found, using default language {self.default_language}")
            lang_code = self.default_language
            
        # Si el idioma por defecto no está cargado, devolver la clave
        if self.default_language not in self.languages:
            print(f"Default language {self.default_language} not loaded")
            return key
            
        # Obtener el texto traducido o la clave si no existe traducción
        return self.languages[lang_code].get(key, self.languages[self.default_language].get(key, key))

# Crear una instancia global
lang_manager = LanguageManager()