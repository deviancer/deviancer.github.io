---
layout: section
title: 分类
eyebrow: BLOG / CATEGORIES
intro: 按主题浏览文章。
permalink: /categories/
---
<div class="archive-groups">{% for category in site.categories %}<section class="archive-group"><h2 id="{{ category[0] | slugify }}">{{ category[0] }}</h2><ul>{% for post in category[1] %}<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><time>{{ post.date | date: '%Y.%m.%d' }}</time></li>{% endfor %}</ul></section>{% endfor %}</div>
