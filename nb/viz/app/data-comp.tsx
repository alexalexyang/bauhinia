import { promises as fs, readdirSync, readFileSync } from 'fs';
import Image from 'next/image';
import Table from './table';

type Stocks = Record<string, {
    info?: {
        companyName: string,
        symbol: string,
        latestPrice?: string,
        trailingPE?: string,
        forwardPE?: string,
        pegRatio?: string,
        trailingPegRatio?: string,
        beta?: string,
    },
    erDates: Record<string, string>[],
    recs: Record<string, string>[],
    graph?: {
        url: string;
        alt: string;
    }
}>

const dataDir = `${process.cwd()}/app/data`

export default async function DataComp() {
    const stocks: Stocks = {}

    const capDirs = readdirSync(dataDir)

    const tickerPaths = capDirs.map((capDir) => {
        const tickersPath = `${dataDir}/${capDir}`
        const tickers = readdirSync(tickersPath)

        return tickers.map(ticker => {
            const tickerPath = `${tickersPath}/${ticker}`
            return tickerPath
        })
    })

    const filePaths = tickerPaths[0].map((tickerPath) => {
        const symbol = tickerPath.split('/').pop()

        if (!symbol) {
            throw new Error(`No symbol for path: ${tickerPath}`)
        }

        const files = readdirSync(tickerPath)
        return files.map(file => {
            const filePath = `${tickerPath}/${file}`

            if (filePath.includes('graph')) {
                const graphPath = `${tickerPath.split('app').pop()}/${file}`

                stocks[symbol] = { ...stocks[symbol], graph: { url: graphPath, alt: `Graph for ${symbol}` } }
            }

            if (filePath.includes('info.json')) {
                const buffer = readFileSync(filePath);
                const info = JSON.parse(buffer.toString())
                stocks[symbol] = { ...stocks[symbol], info }
            }

            if (filePath.includes('er_dates.json')) {
                const buffer = readFileSync(filePath);
                const { data: erDates } = JSON.parse(buffer.toString())
                stocks[symbol] = { ...stocks[symbol], erDates }
            }

            if (filePath.includes('recs.json')) {
                const buffer = readFileSync(filePath);
                const recs = JSON.parse(buffer.toString())
                stocks[symbol] = { ...stocks[symbol], recs }
            }

            return filePath
        })
    })

    const stocksList = Object.values(stocks)

    return (
        <div style={{
            display: "flex",
            flexDirection: "column",
            gap: "1rem",
        }}>
            <h1>Stock data</h1>

            <ul style={{
                display: "flex",
                gap: "4rem",
                flexWrap: "wrap",
                listStyle: "none",
            }}>
                {stocksList.map((stock) => (
                    <li key={stock.info?.["symbol"]}>

                        <div style={{
                            display: "flex",
                            flexDirection: "column",
                            gap: "1rem",
                            width: "555px",
                            border: "1px solid #7e7e7e",
                            borderRadius: "0.5rem",
                            backgroundColor: "#3c3c3c",
                        }}>
                            {stock.graph?.url
                                ? <div style={{
                                    display: "flex",
                                    justifyContent: "center",
                                }}>
                                    <Image
                                        src={require(`.${stock.graph.url}`).default}
                                        alt={stock.graph.alt}
                                        height={300}
                                        width={555}
                                        style={{
                                            borderTopLeftRadius: "0.5rem",
                                            borderTopRightRadius: "0.5rem",
                                        }}
                                    />
                                </div>
                                : <p>No graph</p>}

                            <div style={{ margin: "1rem" }}>
                                <Table data={stock.info!} />
                            </div>

                            {
                                stock.recs?.length
                                    ? <div style={{ margin: "1rem" }}>
                                        {stock.recs.map((rec, idx) => (
                                            <Table data={rec} key={idx} />
                                        ))}
                                    </div>
                                    : null
                            }

                            {
                                stock.erDates?.length
                                    ? <div style={{ margin: "1rem" }}>
                                        {stock.erDates.map((dates, idx) => (
                                            <Table data={dates} key={idx} />
                                        ))}
                                    </div>
                                    : null
                            }

                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}