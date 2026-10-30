---
layout: section
title: 标签
eyebrow: BLOG / TAGS
intro: 用标签找到相近的记录。
permalink: /tags/
---
<div class="tag-cloud">{% for tag in site.tags %}<a class="tag-label" href="#{{ tag[0] | slugify }}">{{ tag[0] }}</a>{% endfor %}</div><div class="archive-groups">{% for tag in site.tags %}<section class="archive-group"><h2 id="{{ tag[0] | slugify }}">{{ tag[0] }}</h2><ul>{% for post in tag[1] %}<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><time>{{ post.date | date: '%Y.%m.%d' }}</time></li>{% endfor %}</ul></section>{% endfor %}</div>
