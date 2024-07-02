<p align="center">
    <a href="https://github.com/psnosignaluk/hangover53">
        <img src="https://raw.githubusercontent.com/psnosignaluk/hangover53/main/docs/img/53.png" alt="Hangover 53" />
    </a>
</p>
<p align="center"><em>Hunt down pesky orphaned DNS records in AWS.</em></p>

Hangover53 is inspired by a hangover from orphaned DNS records. This code would be run in a container, either on k8s
or Fargate, that scrapes DNS and goes hunting for a map between record and resource. When it can't find a home for a
record, it'll complain.

---
