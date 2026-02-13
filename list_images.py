#!/usr/bin/env python3
"""
Helper script to list all images referenced in posts
"""

import os
import re

def find_images_in_posts(posts_dir='_posts'):
    """Find all images referenced in post files"""
    
    images = set()
    
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find header_image in frontmatter
                header_match = re.search(r'header_image:\s*"([^"]+)"', content)
                if header_match:
                    images.add(header_match.group(1))
                
                # Find images in HTML img tags
                img_matches = re.findall(r'<img[^>]+src="([^"]+)"', content)
                images.update(img_matches)
                
                # Find images in markdown syntax
                md_matches = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', content)
                images.update(md_matches)
    
    return sorted(images)

def main():
    print("Images referenced in posts:\n")
    print("="*50)
    
    images = find_images_in_posts()
    
    for img in images:
        print(f"  {img}")
    
    print("="*50)
    print(f"\nTotal: {len(images)} images")
    print(f"\nCopy these files to: assets/images/")
    print(f"\nFrom your original site directory, run:")
    print(f"  cp progress.png gantt2.png names.jpg ... assets/images/")

if __name__ == '__main__':
    main()
