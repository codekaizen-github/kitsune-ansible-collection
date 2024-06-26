# Code_Kaizen Kitsune Collection

This repository contains the `code_kaizen.kitsune` Ansible Collection.

## INSTRUCTIONS FOR USING THIS TEMPLATE

- [ ] Create a new repository on GitHub, selecting this repo to use as the template.
  - [ ] [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- [ ] Clone the repository to your local machine.
- [ ] Search replace these terms to match your collection name and organization
  - [ ] `code_kaizen.kitsune`
  - [ ] `code_kaizen`
  - [ ] `kitsune`
  - [ ] `Code_Kaizen`
  - [ ] `Kitsune`
  - [ ] `code-kaizen`
  - [ ] `kitsune`
- [ ] Remove these instructions from the README.

<!--start requires_ansible-->
<!--end requires_ansible-->

## External requirements

Some modules and plugins require external libraries. Please check the requirements for each plugin or module you use in the documentation to find out which requirements are needed.

## Included content

Please check the included content on the [Ansible Galaxy page for this collection](https://galaxy.ansible.com/code_kaizen/kitsune).

<!--start collection content-->
<!--end collection content-->

## Using this collection

```
    ansible-galaxy collection install code_kaizen.kitsune
```

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
  - name: code_kaizen.kitsune
```

To upgrade the collection to the latest available version, run the following command:

```bash
ansible-galaxy collection install code_kaizen.kitsune --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax where `X.Y.Z` can be any [available version](https://galaxy.ansible.com/code_kaizen/kitsune):

```bash
ansible-galaxy collection install code_kaizen.kitsune:==X.Y.Z
```

See [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing

### Running Tests

Run all tox integration tests:

```sh
python -m tox --ansible --conf tox-ansible.ini
```

Run tox integration tests for a specific environment:

```sh
python -m tox --conf tox-ansible.ini --ansible -e sanity-py3.12-devel
```

Run tox integration tests for a specific scenario:

```sh
# Unit
python -m tox --conf tox-ansible.ini --ansible --matrix-scope unit
# Integration
python -m tox --conf tox-ansible.ini --ansible --matrix-scope integration
```

Run tox integration tests for a specific environment and a specific scenario:

```sh
# Unit
python -m tox --conf tox-ansible.ini --ansible -e sanity-py3.12-devel --matrix-scope unit
# Integratino
python -m tox --conf tox-ansible.ini --ansible -e sanity-py3.12-devel --matrix-scope integration
```


## Release notes

See the [changelog](https://github.com/codekaizen-github/kitsune-ansible-collection/tree/main/CHANGELOG.rst).

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

<!-- List out where the user can find additional information, such as working group meeting times, slack/IRC channels, or documentation for the product this collection automates. At a minimum, link to: -->

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/devel/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
- [Ansible Collections Checklist](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
- [The Bullhorn (the Ansible Contributor newsletter)](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420)
- [News for Maintainers](https://github.com/ansible-collections/news-for-maintainers)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
