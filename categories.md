---
layout: collection
title: 分类
collection: categories
permalink: /categories/
---

<p>所有分类列表，点击分类查看相关文章：</p>

{% capture site_categories %}{% for category in site.categories %}{{ category | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
{% assign sorted_categories = site_categories | split:',' | sort %}

<div class="category-cloud">
{% for category in sorted_categories %}
  <a href="{{ site.url }}{{ site.baseurl }}/categories/#{{ category }}" class="category-link" title="{{ category }}">{{ category }}</a>
{% endfor %}
</div>

<style>
.category-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 20px 0;
}
.category-link {
  padding: 5px 12px;
  background: #4a4a4a;
  border-radius: 4px;
  text-decoration: none;
  color: #fff;
  font-size: 14px;
  transition: background 0.3s;
}
.category-link:hover {
  background: #6a6a6a;
}
</style>

<hr>

<h2>按分类浏览文章</h2>

{% for category in sorted_categories %}
<section id="{{ category }}">
  <h3>{{ category }}</h3>
  <ul>
  {% for post in site.categories[category] %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> - <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%Y年%m月%d日" }}</time></span></li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
