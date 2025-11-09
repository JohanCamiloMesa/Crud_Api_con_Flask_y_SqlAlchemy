import requests
from typing import Optional, Dict, List, Any

class MangaverseAPI:
    """
    Servicio para interactuar con la API de Mangaverse
    """
    BASE_URL = "https://mangaverse-api.p.rapidapi.com"
    API_KEY = "88a37b9498msh5fc28ceb6f43225p18a811jsn7df696001185"
    API_HOST = "mangaverse-api.p.rapidapi.com"
    
    def __init__(self):
        self.headers = {
            "x-rapidapi-key": self.API_KEY,
            "x-rapidapi-host": self.API_HOST
        }
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Realiza una petición a la API y maneja errores
        
        Args:
            endpoint: Endpoint de la API
            params: Parámetros de consulta opcionales
            
        Returns:
            Respuesta de la API en formato JSON o diccionario con error
        """
        try:
            url = f"{self.BASE_URL}{endpoint}"
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return {"error": "La solicitud ha excedido el tiempo de espera"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Error en la solicitud: {str(e)}"}
        except Exception as e:
            return {"error": f"Error inesperado: {str(e)}"}
    
    def fetch_manga(self, page: int = 1, genres: Optional[str] = None, 
                    nsfw: bool = True, type_filter: str = "all") -> Dict[str, Any]:
        """
        Obtiene una lista de mangas con filtros opcionales
        
        Args:
            page: Número de página
            genres: Géneros separados por comas (ej: "Harem,Fantasy")
            nsfw: Incluir contenido NSFW
            type_filter: Tipo de manga ("all", "manga", "manhwa", "manhua")
            
        Returns:
            Diccionario con los mangas encontrados
        """
        params = {
            "page": str(page),
            "nsfw": "true" if nsfw else "false",
            "type": type_filter
        }
        
        if genres:
            params["genres"] = genres
            
        return self._make_request("/manga/fetch", params)
    
    def fetch_latest(self, page: int = 1, genres: Optional[str] = None,
                     nsfw: bool = True, type_filter: str = "all") -> Dict[str, Any]:
        """
        Obtiene los mangas más recientes
        
        Args:
            page: Número de página
            genres: Géneros separados por comas
            nsfw: Incluir contenido NSFW
            type_filter: Tipo de manga
            
        Returns:
            Diccionario con los mangas más recientes
        """
        params = {
            "page": str(page),
            "nsfw": "true" if nsfw else "false",
            "type": type_filter
        }
        
        if genres:
            params["genres"] = genres
            
        return self._make_request("/manga/latest", params)
    
    def search_manga(self, text: str, nsfw: bool = True, 
                     type_filter: str = "all") -> Dict[str, Any]:
        """
        Busca mangas por texto
        
        Args:
            text: Texto de búsqueda
            nsfw: Incluir contenido NSFW
            type_filter: Tipo de manga
            
        Returns:
            Diccionario con los resultados de búsqueda
        """
        params = {
            "text": text,
            "nsfw": "true" if nsfw else "false",
            "type": type_filter
        }
        
        return self._make_request("/manga/search", params)
    
    def get_manga(self, manga_id: str) -> Dict[str, Any]:
        """
        Obtiene información detallada de un manga específico
        
        Args:
            manga_id: ID del manga
            
        Returns:
            Diccionario con la información del manga
        """
        params = {"id": manga_id}
        return self._make_request("/manga", params)
    
    def fetch_chapters(self, manga_id: str) -> Dict[str, Any]:
        """
        Obtiene los capítulos de un manga
        
        Args:
            manga_id: ID del manga
            
        Returns:
            Diccionario con los capítulos del manga
        """
        params = {"id": manga_id}
        return self._make_request("/manga/chapter", params)
    
    def fetch_images(self, chapter_id: str) -> Dict[str, Any]:
        """
        Obtiene las imágenes de un capítulo específico
        
        Args:
            chapter_id: ID del capítulo
            
        Returns:
            Diccionario con las imágenes del capítulo
        """
        params = {"id": chapter_id}
        return self._make_request("/manga/image", params)


# Instancia única del servicio
manga_api = MangaverseAPI()
