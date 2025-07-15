# GitHub Pages Setup Guide

## 🚀 **Deploy Your Documentation Website**

### **Step 1: Enable GitHub Pages**

1. Go to your GitHub repository
2. Click **Settings** tab
3. Scroll to **Pages** section
4. Under **Source**, select **Deploy from a branch**
5. Choose **main** branch and **docs** folder
6. Click **Save**

### **Step 2: Access Your Website**

Your site will be available at:
```
https://your-username.github.io/educonnect-pro
```

### **Step 3: Custom Domain (Optional)**

1. Add your domain to `docs/CNAME` file
2. Configure DNS settings with your domain provider
3. Point to: `your-username.github.io`

### **Step 4: Update Links**

Update the GitHub links in `docs/index.html`:
```html
<!-- Replace 'your-username' with your actual GitHub username -->
<a href="https://github.com/your-username/educonnect-pro">
```

## ✨ **Features of Your Website**

- **Modern UI**: Clean, professional design
- **Dark Mode**: Toggle between light and dark themes
- **Responsive**: Mobile-friendly layout
- **Fast Loading**: Optimized with Tailwind CSS CDN
- **SEO Ready**: Meta tags and structured content
- **Documentation Hub**: Links to all guides

## 🎨 **Customization**

### **Colors**
Update the primary colors in the Tailwind config:
```javascript
colors: {
    primary: {
        50: '#eff6ff',
        500: '#3b82f6',  // Change this
        600: '#2563eb',  // And this
        // ...
    }
}
```

### **Content**
- Update hero section text
- Add your GitHub username to links
- Customize feature descriptions
- Add your own branding

### **Analytics (Optional)**
Add Google Analytics by inserting tracking code before `</head>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_TRACKING_ID');
</script>
```

## 🔧 **Maintenance**

### **Update Documentation**
1. Edit markdown files in `docs/` folder
2. Commit and push changes
3. GitHub Pages will automatically rebuild

### **Add New Pages**
1. Create new `.md` or `.html` files in `docs/`
2. Link them from `index.html`
3. Follow the same styling patterns

Your professional documentation website is ready! 🎉