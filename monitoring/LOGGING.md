#  Logging report

## How to start

### Install

```shell
docker-compose up #From monitoring folder
```

### Usage

Open [http://localhost:3000](http://localhost:3000/) in your browser to open Grafana. 
Add loki as a source by using URL: ```http://loki:3100```.
After that you can view logs in `Explore` section.

## Best practices

- Using static labels

  Use host, application, and environment as static labels

- Using dynamic labels sparingly

  Use filter expressions instead.

- Bounding label values

  Slattern usage of unbounded/infinite values may lead to big problems.

- Be aware of dynamic labels applied by clients

  Similarly to the second point, be careful with using dynamic labels even when it comes to applying labels by clients.

- Utilize caching

- Logs must be in increasing time order per stream

  Incorrect order of logs may make them disappear or cause different problems.

## Success screenshots

![](\screenshots\Docker state.PNG)

![](\screenshots\Loki.PNG)

(All screenshots are in `screenshots` folder)