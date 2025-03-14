function getRandomImage() {
  fetch("/get_image")
    .then((response) => response.json())
    .then((data) => {
      const imageUrl = "/static/" + data.image_url;
      document.getElementById("random-image").src = imageUrl;
    });
}
