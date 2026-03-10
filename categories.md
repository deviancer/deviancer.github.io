---
layout: page
title: 分类
---

<p>所有分类列表：</p>

{% if site.categories %}
<div class="tag-cloud">
{% for category in site.categories %}
  <a href="#{{ category[0] }}" class="tag-label">{{ category[0] }}</a>
{% endfor %}
</div>

<hr>

<h2>按分类浏览文章</h2>

{% for category in site.categories %}
<section id="{{ category[0] }}">
  <h3>{{ category[0] }}</h3>
  <ul>
  {% for post in category[1] %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> - <time>{{ post.date | date: "%Y年%m月%d日" }}</time></li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
{% else %}
<p>暂无分类</p>
{% endif %}
