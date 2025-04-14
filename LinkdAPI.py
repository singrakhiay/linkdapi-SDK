import httpx


class LinkdAPI:
    """
    A client for interacting with the LinkdAPI, which provides unofficial LinkedIn and Sales Navigator APIs.
    
    Args:
        api_key (str): The RapidAPI key required for authentication.
        base_url (str, optional): The base URL for the API. Defaults to "https://linkdapi.p.rapidapi.com".
    """
    
    def __init__(self, api_key: str, base_url: str = "https://linkdapi.p.rapidapi.com"):
        self.api_key = api_key
        self.base_url = base_url
        self.client = httpx.Client()
        
    def _get_headers(self) -> dict:
        """
        Returns the common headers for API requests.
        """
        return {
            "x-rapidapi-host": "linkdapi.p.rapidapi.com",
            "x-rapidapi-key": self.api_key,
            "content-type": "application/json",
        }
    
    def _send_request(self, method: str, endpoint: str, params: dict = None) -> dict:
        """
        Sends an HTTP request to the API.
        
        Args:
            method (str): The HTTP method (GET, POST, etc.)
            endpoint (str): The API endpoint
            params (dict, optional): Query parameters for the request
            
        Returns:
            dict: The JSON response from the API
            
        Raises:
            httpx.HTTPStatusError: If the request fails
        """
        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers()
        
        response = self.client.request(method, url, headers=headers, params=params)
        response.raise_for_status()
        
        return response.json()

    # Profile Endpoints
    def get_profile_overview(self, username: str) -> dict:
        """
        Get basic profile information by username.
        
        Args:
            username (str): The LinkedIn username to look up
            
        Returns:
            dict: Profile overview data
        """
        endpoint = "api/v1/profile/overview"
        params = {"username": username}
        return self._send_request("GET", endpoint, params)
    
    def get_profile_details(self, urn: str) -> dict:
        """
        Get profile details information by URN.
        
        Args:
            urn (str): The LinkedIn URN (Uniform Resource Name) for the profile
            
        Returns:
            dict: Detailed profile information
        """
        endpoint = "api/v1/profile/details"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)
    
    def get_contact_info(self, username: str) -> dict:
        """
        Get contact details for a profile by username.
        
        Args:
            username (str): The LinkedIn username to look up
            
        Returns:
            dict: Contact information including email, phone, and websites
        """
        endpoint = "api/v1/profile/contact-info"
        params = {"username": username}
        return self._send_request("GET", endpoint, params)
    
    def get_full_experience(self, urn: str) -> dict:
        """
        Get complete work experience by URN.
        
        Args:
            urn (str): The LinkedIn URN for the profile
            
        Returns:
            dict: Complete work experience information
        """
        endpoint = "api/v1/profile/full-experience"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)
    
    def get_certifications(self, urn: str) -> dict:
        """
        Get lists of professional certifications by URN.
        
        Args:
            urn (str): The LinkedIn URN for the profile
            
        Returns:
            dict: Certification information
        """
        endpoint = "api/v1/profile/certifications"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)
    
    def get_education(self, urn: str) -> dict:
        """
        Get full education information by URN.
        
        Args:
            urn (str): The LinkedIn URN for the profile
            
        Returns:
            dict: Education history
        """
        endpoint = "api/v1/profile/education"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)
    
    def get_skills(self, urn: str) -> dict:
        """
        Get profile skills by URN.
        
        Args:
            urn (str): The LinkedIn URN for the profile
            
        Returns:
            dict: Skills information
        """
        endpoint = "api/v1/profile/skills"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)
    
    def get_social_matrix(self, username: str) -> dict:
        """
        Get social network metrics by username.
        
        Args:
            username (str): The LinkedIn username to look up
            
        Returns:
            dict: Social metrics including connections and followers count
        """
        endpoint = "api/v1/profile/social-matrix"
        params = {"username": username}
        return self._send_request("GET", endpoint, params)
    
    def get_recommendations(self, urn: str) -> dict:
        """
        Get profile given and received recommendations by URN.
        
        Args:
            urn (str): The LinkedIn URN for the profile
            
        Returns:
            dict: Recommendations data
        """
        endpoint = "api/v1/profile/recommendations"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)
    
    def get_similar_profiles(self, urn: str) -> dict:
        """
        Get similar profiles for a given profile using its URN.
        
        Args:
            urn (str): The LinkedIn URN for the profile
            
        Returns:
            dict: List of similar profiles
        """
        endpoint = "api/v1/profile/similar"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)
    
    def get_profile_about(self, urn: str) -> dict:
        """
        Get about this profile such as last update and verification info.
        
        Args:
            urn (str): The LinkedIn URN for the profile
            
        Returns:
            dict: Profile about information
        """
        endpoint = "api/v1/profile/about"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)
    
    def get_profile_reactions(self, urn: str, cursor: str = "") -> dict:
        """
        Get all reactions for given profile by URN.
        
        Args:
            urn (str): The LinkedIn URN for the profile
            cursor (str, optional): Pagination cursor
            
        Returns:
            dict: Reactions data with pagination information
        """
        endpoint = "api/v1/profile/reactions"
        params = {"urn": urn}
        if cursor:
            params["cursor"] = cursor
        return self._send_request("GET", endpoint, params)
    
    # Posts Endpoints
    def get_featured_posts(self, urn: str) -> dict:
        """
        Get all featured posts for a given profile using its URN.
        
        Args:
            urn (str): The LinkedIn URN for the profile
            
        Returns:
            dict: List of featured posts
        """
        endpoint = "api/v1/posts/featured"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)
    
    def get_all_posts(self, urn: str, cursor: str = "", start: int = 0) -> dict:
        """
        Retrieve all posts for a given profile URN.

        Args:
            urn (str): The LinkedIn URN of the profile.
            cursor (str, optional): Pagination cursor (default is empty).
            start (int, optional): Start index for pagination (default is 0).

        Returns:
            dict: List of posts with pagination info.
        """
        endpoint = "api/v1/posts/all"
        params = {"urn": urn, "cursor": cursor, "start": start}
        return self._send_request("GET", endpoint, params)

    def get_post_info(self, urn: str) -> dict:
        """
        Retrieve information about a specific post using its URN.

        Args:
            urn (str): The URN of the LinkedIn post.

        Returns:
            dict: Detailed post information.
        """
        endpoint = "api/v1/posts/info"
        params = {"urn": urn}
        return self._send_request("GET", endpoint, params)

    def get_post_comments(self, urn: str, start: int = 0, count: int = 10, cursor: str = "") -> dict:
        """
        Get comments for a specific LinkedIn post.

        Args:
            urn (str): The URN of the post.
            start (int, optional): Starting index for pagination.
            count (int, optional): Number of comments to fetch per request.
            cursor (str, optional): Cursor for pagination (default is empty).

        Returns:
            dict: A list of comments and pagination metadata.
        """
        endpoint = "api/v1/posts/comments"
        params = {"urn": urn, "start": start, "count": count, "cursor": cursor}
        return self._send_request("GET", endpoint, params)

    def get_post_likes(self, urn: str, start: int = 0) -> dict:
        """
        Retrieve all users who liked or reacted to a given post.

        Args:
            urn (str): The URN of the LinkedIn post.
            start (int, optional): Pagination start index (default is 0).

        Returns:
            dict: List of users who liked/reacted to the post.
        """
        endpoint = "api/v1/posts/likes"
        params = {"urn": urn, "start": start}
        return self._send_request("GET", endpoint, params)

    # Comments Endpoints
    def get_all_comments(self, urn: str, cursor: str = "") -> dict:
        """
        Retrieve all comments made by a profile using their URN.

        Args:
            urn (str): The LinkedIn profile URN.
            cursor (str, optional): Pagination cursor (default is empty).

        Returns:
            dict: List of comments made by the user.
        """
        endpoint = "api/v1/comments/all"
        params = {"urn": urn, "cursor": cursor}
        return self._send_request("GET", endpoint, params)

    def get_comment_likes(self, urns: str, start: int = 0) -> dict:
        """
        Get all users who reacted to one or more comment URNs.

        Args:
            urns (str): Comma-separated URNs of comments.
            start (int, optional): Pagination start index (default is 0).

        Returns:
            dict: List of users who liked or reacted to the comments.
        """
        endpoint = "api/v1/comments/likes"
        params = {"urn": urns, "start": start}
        return self._send_request("GET", endpoint, params)

    # Service Status Endpoint
    def get_service_status(self) -> dict:
        endpoint = "status"
        return self._send_request("GET", endpoint)
    
    def __del__(self):
        """Clean up the HTTP client when the instance is destroyed."""
        self.client.close()
