---
layout: default
title: 日志
---

<h1>所有文章</h1>

<ul class="posts">
{% for post in site.posts %}
  <li class="post-item">
    <a href="{{ post.url | relative_url }}" class="post-link">
      <div class="post-title-row">
        <h2 class="post-title">{{ post.title }}</h2>
        <time class="post-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y年%m月%d日" }}</time>
      </div>
      {% if post.tags %}
      <p class="post-tags-row">{% for tag in post.tags %}<span class="tag">{{ tag }}</span>{% endfor %}</p>
      {% endif %}
    </a>
  </li>
{% endfor %}
</ul>
