import argostranslate.package

available_packages = argostranslate.package.get_available_packages()

package_to_install = next(
    filter(
        lambda x: x.from_code == "en" and x.to_code == "fr",
        available_packages
    )
)

download_path = package_to_install.download()

argostranslate.package.install_from_path(download_path)

print("Installation terminée : Anglais → Français")