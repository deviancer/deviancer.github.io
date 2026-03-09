---
layout: default
title: 日志
---

<h1>所有文章</h1>

<ul class="posts">
{% for post in site.posts %}
  <li class="post-item">
    <a href="{{ post.url | relative_url }}" class="post-link">
      <h2 class="post-title">{{ post.title }}</h2>
      <p class="post-meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y年%m月%d日" }}</time>
        {% if post.tags %}
         | 标签: {% for tag in post.tags %}{{ tag }}{% endfor %}
        {% endif %}
      </p>
    </a>
  </li>
{% endfor %}
</ul>
