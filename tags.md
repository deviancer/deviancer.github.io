---
layout: page
title: 标签
---

<p>所有标签列表：</p>

{% if site.tags %}
<div class="tag-cloud">
{% for tag in site.tags %}
  <a href="#{{ tag[0] }}" class="tag-label">{{ tag[0] }}</a>
{% endfor %}
</div>

<hr>

<h2>按标签浏览文章</h2>

{% for tag in site.tags %}
<section id="{{ tag[0] }}">
  <h3>{{ tag[0] }}</h3>
  <ul>
  {% for post in tag[1] %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> - <time>{{ post.date | date: "%Y年%m月%d日" }}</time></li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
{% else %}
<p>暂无标签</p>
{% endif %}
