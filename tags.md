---
layout: collection
title: 标签
collection: tags
permalink: /tags/
---

<p>所有标签列表，点击标签查看相关文章：</p>

{% capture site_tags %}{% for tag in site.tags %}{{ tag | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
{% assign sorted_tags = site_tags | split:',' | sort %}

<div class="tag-cloud">
{% for tag in sorted_tags %}
  <a href="{{ site.url }}{{ site.baseurl }}/tags/#{{ tag }}" class="tag-link" title="{{ tag }}">#{{ tag }}</a>
{% endfor %}
</div>

<style>
.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 20px 0;
}
.tag-link {
  padding: 5px 12px;
  background: #333;
  border-radius: 4px;
  text-decoration: none;
  color: #fff;
  font-size: 14px;
  transition: background 0.3s;
}
.tag-link:hover {
  background: #5a5a5a;
}
</style>

<hr>

<h2>按标签浏览文章</h2>

{% for tag in sorted_tags %}
<section id="{{ tag }}">
  <h3>#{{ tag }}</h3>
  <ul>
  {% for post in site.tags[tag] %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> - <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%Y年%m月%d日" }}</time></span></li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
