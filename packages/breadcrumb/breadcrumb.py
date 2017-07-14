from lektor.context import site_proxy

def breadcrumb_for_page(page, sep=None):
    """
    Filter for creating lektor page breadcrumb

    :param page: the :class:`~lektor.db.Record` instance of page
    :param sep: optionally provided string separator

    """
    parts = page.path.split('/')
    breadcrumb = u''
    for i,part in enumerate(parts):
        link_parts = []
        for cnt in range(0, i+1):
            link_parts.append(parts[cnt])
        href = '/'.join(link_parts)
        if href == '':
            href = '/'
        part = site_proxy.get(href, alt=page.alt)
        breadcrumb += u'<a href="%s">%s</a>%s' % (part.path, part.path, sep)
    return breadcrumb

