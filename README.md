### **README.md**

# Ubuntu Requests – Ubuntu-Inspired Image Fetcher

> *"I am because we are." – Ubuntu Philosophy*

## **Project Overview**

Ubuntu emphasizes **community, respect, and sharing**. This Python script reflects that spirit by connecting to the global internet community to respectfully fetch shared images, organize them, and make them accessible for later appreciation.

The script allows users to:

* Download one or multiple images from given URLs
* Automatically organize them into a `Fetched_Images` folder
* Prevent duplicate downloads
* Gracefully handle network and file errors
* Ensure only valid images are saved

---

## **Features**

* **Multiple URL support** – Download several images in one go.
* **Duplicate prevention** – Skips already downloaded images.
* **Content-Type validation** – Only fetches valid images.
* **Auto filename generation** – Uses URL-based names or a unique fallback.
* **Error handling** – Handles network errors, timeouts, and invalid URLs.

---

## **Installation & Setup**

### Prerequisites

* Python 3.x installed
* `requests` library installed

### Install Dependencies

```bash
pip install requests
```

### Clone Repository

```bash
git clone https://github.com/your-username/Ubuntu-Requests.git
cd Ubuntu-Requests
```

---

## **Usage**

Run the script:

```bash
python ubuntu_image_fetcher.py
```

Enter one or multiple image URLs separated by commas:

```
https://example.com/ubuntu-wallpaper.jpg, https://example.com/another-image.png
```

Example output:

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.
```

---

## **Ubuntu Principles in Action**

* **Community** – Connects with the web to gather shared images.
* **Respect** – Handles errors gracefully, avoiding crashes.
* **Sharing** – Organizes images for later sharing or reuse.
* **Practicality** – A simple tool with real-world utility.

---

## **Future Enhancements**

* Add file size checks before downloading
* Include user-defined download limits
* Support for different image formats (e.g., `.webp`)
* Logging system for fetched images

---

## **License**

This project is open-source under the MIT License.

---


