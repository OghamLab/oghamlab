# Deploy OghamLab to GitHub Pages

## Before publishing
- The Frontis Privacy Policy currently contains a visible **Review before publishing** notice. Verify permissions, third-party services, data retention, and Google Play Data safety disclosures before treating it as final.
- Confirm support@oghamlab.com receives mail.
- No Google Play download button has been added.

## Publish
1. Create a public GitHub repository named `oghamlab.github.io` under the `oghamlab` account, or use an existing repository whose Pages site will serve the custom domain. Do not overwrite an existing repository without checking its contents.
2. Place the contents of this `OghamLab` directory in the **root** of the repository, including `CNAME` and `index.html`.
3. From this directory, if starting a new repository:
   ```sh
   git init
   git add .
   git commit -m "Deploy OghamLab Frontis website"
   git branch -M main
   git remote add origin https://github.com/oghamlab/oghamlab.github.io.git
   git push -u origin main
   ```
   If the repository already exists, clone it first and copy these website files into the clone, then commit and push. Do not reinitialize or force-push.
4. On GitHub: repository Settings > Pages > Build and deployment > Deploy from a branch > `main` / `(root)` > Save.
5. In Settings > Pages set custom domain to `oghamlab.com`, if not already configured.
6. Confirm Namecheap DNS has four apex A records for 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 and a `www` CNAME pointing to `oghamlab.github.io`.
7. After GitHub's DNS check and certificate provisioning, enable Enforce HTTPS.
8. Verify /, /frontis/, /frontis/privacy/, /frontis/support/ and mobile navigation.

## Local preview
Run `python3 -m http.server 8000` from this directory, then open http://localhost:8000/frontis/.
