# Shorten.URls

- ### This is a URL-Shortener + Ananlysis web-app.
- ### Features : 
    - users can shorten their URL by providing their own urls.
    - users can get analysis of how their URL is being shared.
    - currently URL analysis includes total number of clicks on link, country-wise, region-wise, city-wise split of all URL hits.
    - analysis data also includes hour-wise split of all link clicks.
    - this data can be used to analyse and effectively identify user-demographics and user-patterns.


### Documentation : 

Access API documentation here : [PostMan Documentation](https://documenter.getpostman.com/view/17713936/UzQuP5pq)

### Future Development Ideas:
- allow users to get custom shortended URLs.
- introduce Redis caching for better performance.
- integrate Celery for processing tasks asynchronously(outside of request-response cycle).
- build out frontend to graphically present analysis.

Contributions are always welcome!!!

### Notes : 
- timestamps are in seconds.
- all timestamps are Epoch Unix Timstamp(UTC).