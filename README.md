# African BirdLife Scraper

A ChatGPT generated scraping script to download the magazine archive of African BirdLife.

### Run it

```shell
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip3 install -r requirements.txt

# Run it
python3 main.py
```


### ChatGPT prompt

This was the first prompt to get ChatGPT going (using GPT-3.5 - ChatGPT July 20 Version in 2023)

> Hi python bot! Please help me write a python script that uses the `scrapy` library to download archived magazine sections from a website. When navigating to `https://www.birdlife.org.za/african-birdlife-index/`, the page is split up in sections, grouped by year. Each 'year' div has CSS class "vc_tta-panel". Each magazine in a year group is located in a div with CSS classes "wpb_column vc_column_container vc_col-sm-2". Once the magazine is clicked, a new page opens up with a div with CSS class "wpb_wrapper", which contains a deeply nested list of < a> tags with property "data-downloadurl". Clicking the URL in this value will then download the magazine section PDF. Below is an example of the div with "wpb_wrapper" CSS class:

```html
<div class="wpb_wrapper">
	<div class="w3eden"><!-- WPDM Link Template: Default Template -->
		<div class="link-template-default card mb-2">
    <div class="card-body">
        <div class="media stack-xs">
            <div class="media-body">
                <div class="media">
                    <div class="media-body">
                        <h3 class="package-title"><a href="https://www.birdlife.org.za/download/monitoring-our-dynamic-planet/">Monitoring our dynamic planet</a></h3>
                        <div class="text-muted text-small"><i class="fas fa-hdd ml-3"></i> 286 KB</div>
                    </div>
                </div>
            </div>
            <div class="ml-3 wpdmdl-btn">
                <a class="wpdm-download-link download-on-click btn btn-primary " rel="nofollow" href="#" data-downloadurl="https://www.birdlife.org.za/download/monitoring-our-dynamic-planet/?wpdmdl=34899&amp;refresh=64c6595e506631690720606">Download</a>
            </div>
        </div>
    </div>
</div>
	</div><br>
</div>
```
