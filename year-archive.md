---
layout: archive
title: 日志归档
permalink: /year-archive/
---

<h2>按年份浏览</h2>

{% assign years = "" %}
{% for post in site.posts %}
  {% capture year %}{{ post.date | date: "%Y" }}{% endcapture %}
  {% unless years contains year %}
    {% assign years = years | append: year | append: "," %}
  {% endunless %}
{% endfor %}

{% assign sorted_years = years | split:"," | sort | reverse %}

{% for year in sorted_years %}
<section id="{{ year }}">
  <h3>{{ year }}年</h3>
  <ul>
  {% for post in site.posts %}
    {% assign post_year = post.date | date: "%Y" %}
    {% if post_year == year %}
      <li><a href="{{ post.url }}">{{ post.title }}</a> - <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%m月%d日" }}</time></span></li>
    {% endif %}
  {% endfor %}
  </ul>
</section>
{% endfor %}
