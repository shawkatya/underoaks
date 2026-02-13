# Under the Oaks - Jekyll Site

A Jekyll blog about the Ukrainian village Piddubtsi, converted from a single-page HTML site.

## Setup

### 1. Install Ruby and Jekyll

**Windows:**
- Download and install Ruby from [rubyinstaller.org](https://rubyinstaller.org/)
- Run: `gem install jekyll bundler`

**Mac:**
- Ruby comes pre-installed
- Run: `gem install jekyll bundler`

**Linux:**
- Run: `sudo apt-get install ruby-full build-essential`
- Run: `gem install jekyll bundler`

### 2. Install Dependencies

```bash
cd jekyll_site
bundle install
```

### 3. Add Your Images

Copy all your images from the original site to:
```
assets/images/
```

Make sure these files are present:
- progress.png, gantt2.png
- names.jpg
- photos.jpg, palace1.jpg, palace2.jpg, palace3.jpg, park.jpg, church.jpg, blog1.jpg, blog2.jpg, blog3.jpg, wwi.jpg
- maps.jpg, karta.jpg, visicom.png, imisto.png, satellite.png, mapcartasat.png, mapcarta.png, mig2.jpg, soviet.png, austrian.png, arcanum.jpg
- main.jpg
- whois.jpg
- Any other images referenced in your posts

### 4. Run Locally

```bash
bundle exec jekyll serve
```

Then visit: `http://localhost:4000`

### 5. Deploy to GitHub Pages

1. Create a new GitHub repository (e.g., `underoaks`)

2. Update `_config.yml`:
   ```yaml
   url: "https://yourusername.github.io"
   baseurl: "/underoaks"
   ```

3. Push to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/underoaks.git
   git push -u origin main
   ```

4. Enable GitHub Pages:
   - Go to repository Settings → Pages
   - Source: Deploy from branch `main`
   - Save

5. Your site will be live at: `https://yourusername.github.io/underoaks/`

## File Structure

```
jekyll_site/
├── _config.yml          # Site configuration
├── _layouts/            # Page templates
│   ├── default.html     # Main layout with header/sidebar
│   └── post.html        # Individual post layout
├── _posts/              # Blog posts (markdown files)
├── assets/
│   └── images/          # All images go here
├── index.html           # Homepage (lists all posts)
├── Gemfile              # Ruby dependencies
└── .gitignore           # Files to ignore in git
```

## Adding New Posts

Create a new file in `_posts/` with the format:
```
YYYY-MM-DD-title-of-post.md
```

With frontmatter:
```yaml
---
layout: post
title: "Post Title"
date: 2026-01-15 12:00:00
subtitle: "Brief description"
header_image: "image.jpg"
post_id: "unique-id"
---

Your content here...
```

## Customization

- **Colors/Styling**: Edit the `<style>` section in `_layouts/default.html`
- **Sidebar**: Edit the sidebar section in `_layouts/default.html`
- **Footer**: Edit the footer in `_layouts/default.html`
- **Site info**: Edit `_config.yml`

## Notes

- Posts are sorted by date (newest first on homepage)
- The W3.CSS framework is loaded from CDN
- Images should use relative paths: `{{ site.baseurl }}/assets/images/filename.jpg`
- HTML content is preserved in posts for tables, complex formatting, etc.
