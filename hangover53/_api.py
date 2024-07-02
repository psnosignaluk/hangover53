import dns.resolver


def resolve(record_types, target_domain):
    resolver = dns.resolver.Resolver()
    for record_type in record_types:
        try:
            answers = resolver.resolve(target_domain, record_type)
        except dns.resolver.NoAnswer:
            continue

        print(f"{record_type} records for {target_domain}")
        for rdata in answers:
            print(f"{rdata}")
