"""
cli.py — Winamus Document Generator CLI
Usage: python cli.py generate --help
"""
import click
from pathlib import Path
from .generator import generate
from .config import get_config


@click.group()
def cli():
    """🗂️  Winamus Document Generator — CLI"""
    pass


@cli.command()
@click.option("--source", "-s", required=True, type=click.Path(exists=True), help="Path ke file Markdown sumber")
@click.option("--type", "-t", "doc_type", required=True,
              type=click.Choice(["quotation", "invoice", "proposal", "contract", "bast", "cover_letter"]),
              help="Tipe dokumen")
@click.option("--style", default="modern",
              type=click.Choice(["modern", "classic", "bold"]),
              show_default=True, help="Visual style")
@click.option("--layout", "-l", default=None, help="Layout varian (table/narrative/dll)")
@click.option("--format", "-f", "formats", multiple=True,
              type=click.Choice(["pdf", "docx", "html"]),
              help="Format output (bisa lebih dari satu). Default: semua")
@click.option("--output", "-o", default=None, type=click.Path(), help="Folder output (default: output/)")
@click.option("--project", "-p", default=None, type=click.Path(), help="Path ke project/xxx/Docs/ untuk salin hasil ke sana")
@click.option("--all-formats", "all_formats", is_flag=True, default=False, help="Generate semua format (pdf, docx, html)")
def generate_cmd(source, doc_type, style, layout, formats, output, project, all_formats):
    """Generate dokumen dari file Markdown."""
    cfg = get_config()

    # Default layout berdasarkan doc_type
    if not layout:
        layout = cfg["document_types"][doc_type]["default_layout"]

    # Format
    if all_formats or not formats:
        formats = ["pdf", "docx", "html"]

    click.echo(f"\n🔄 Generating: {Path(source).name}")
    click.echo(f"   Type: {doc_type} | Style: {style} | Layout: {layout}")
    click.echo(f"   Formats: {', '.join(formats)}\n")

    try:
        results = generate(
            source_path=source,
            doc_type=doc_type,
            style=style,
            layout=layout,
            formats=list(formats),
            output_dir=output,
            project_docs_dir=project,
        )

        for fmt, path in results.items():
            size_kb = path.stat().st_size / 1024
            click.echo(f"   ✅ {fmt.upper():5s} → {path}  ({size_kb:.1f} KB)")

        click.echo(f"\n✨ Done! {len(results)} file(s) generated.\n")

    except Exception as e:
        click.echo(f"\n❌ Error: {e}\n", err=True)
        raise SystemExit(1)


@cli.command("list-templates")
def list_templates():
    """Tampilkan semua template (styles & layouts) yang tersedia."""
    cfg = get_config()
    click.echo("\n📋 Available Templates\n")

    click.echo("  Visual Styles:")
    for s in ["modern", "classic", "bold"]:
        click.echo(f"    • {s}")

    click.echo("\n  Document Types & Layouts:")
    for dtype, info in cfg["document_types"].items():
        layouts = ", ".join(info["layouts"])
        click.echo(f"    • {dtype:15s} [{layouts}]  — {info['label']}")

    click.echo()


@cli.command()
def info():
    """Tampilkan info konfigurasi perusahaan aktif."""
    cfg = get_config()
    co = cfg["company"]
    click.echo(f"\n🏢 {co['name']} ({co['brand']})")
    click.echo(f"   Website : {co['website']}")
    click.echo(f"   Email   : {co['email']}")
    click.echo(f"   Phone   : {co['phone']}")
    click.echo(f"   NPWP    : {co['npwp']}")
    click.echo(f"   Bank    : {co['bank']} — {co['account_number']}")
    click.echo()


if __name__ == "__main__":
    cli()
