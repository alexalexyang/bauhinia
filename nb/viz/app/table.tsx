type Props = {
    data: Record<string, string>
}

export default function Table({ data }: Props) {
    return (
        <table style={{
            width: '100%',
        }}>
            <tbody>
                {Object.entries(data).map(([key, value]) => (
                    <tr key={key}>
                        <div style={{
                            width: '100%',
                            display: 'flex',
                            justifyContent: 'space-between',
                            borderBottom: '1px solid #7e7e7e',
                            padding: '0.5rem 0',
                            fontSize: '1.2rem',
                        }}>
                            <th>{key}</th>
                            <td style={{
                                width: '50%',
                            }}
                            >{value}</td>
                        </div>
                    </tr>


                ))}
            </tbody>
        </table>
    )
}